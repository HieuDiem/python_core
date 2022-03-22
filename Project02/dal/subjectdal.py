from dot import SubjectDot
from .dbprovider import DBProvider

class SubjectDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    # tao bang neu chua ton tai
    def __createTableIfNotExists(self):#TODO bs update,delete oncade
        sql = """
            CREATE TABLE IF NOT EXISTS Subjects(
                SubjectID Varchar(6) PRIMARY KEY,
                SubName Varchar(20) NOT NULL
        )
        """
        self.__dbProvider.exec(sql)

    # them mon hoc
    def insert(self, sbj: SubjectDot):
        sql = """
            INSERT INTO Subjects(SubjectID, SubName)
            VALUES(%s, %s)
        """
        params = (sbj.SubjectID, sbj.SubName)
        return self.__dbProvider.exec(sql, params)

    # sua thong tin mon hoc
    def update(self, sbj: SubjectDot):
        sql = """
            UPDATE Subjects
            SET
                SubName = %s
            WHERE SubjectID = %s
        """
        params = (sbj.SubName, sbj.SubjectID)
        return self.__dbProvider.exec(sql, params)

    # xoa thong tin mon hoc
    def delete(self, subjectID: str):
        sql = """
            DELETE FROM Subjects
            WHERE SubjectID = %s
        """
        params = (subjectID,)
        return self.__dbProvider.exec(sql,params)

    #lay nhieu ban ghi
    def get(self):
        sql = """
            SELECT * FROM Subjects
        """
        subjects = self.__dbProvider.get(sql)
        subjectDots = list(map(lambda sbj: SubjectDot(sbj[0], sbj[1]), subjects))
        return subjectDots

    # lay 1 ban ghi
    def getOne(self, subjectID: str):
        sql = """
            SELECT * FROM Subjects
            WHERE SubjectID = %s
        """
        params = (subjectID)
        subject = self.__dbProvider.getOne(sql, params)
        subjectDot = SubjectDot(subject[0], subject[1])
        return subjectDot

    # tim kiem mon hoc
    def search(self, text: str):
        sql = """"
            SELECT * FROM Subjects
            WHERE SubjectID = %s OR SubName LIKE %s
        """
        params = (text, f'%{text}%')
        subjects = self.__dbProvider.get(sql, params)
        subjectDots = list(map(lambda sbj: SubjectDot(sbj[0], sbj[1]), subjects)) 
        return subjectDots

    # kiem tra su ton tai mon hoc
    def checkExists(self, subjectID: str):
        isExists = False
        sql = """
            SELECT * FROM Subjects
            WHERE SubjectID = %s
        """
        params = (subjectID,)
        subject = self.__dbProvider.getOne(sql, params)
        print(subject)
        if subject is not None:
            isExists = True
        return isExists
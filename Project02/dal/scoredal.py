from operator import index
from dot import ScoreDot, ScoreExportDot
from .dbprovider import DBProvider
import pandas as pd

class ScoreDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    #tao bang neu chua ton tai
    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Scores(
                StudentID Varchar(6),
                SubjectID Varchar(6),
                Score1 int NOT NULL,
                Score2 int NOT NULL,
                PRIMARY KEY (StudentID, SubjectID),
                FOREIGN KEY (StudentID) REFERENCES Students(studentID) ON DELETE CASCADE,
                FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID) ON DELETE CASCADE
            )
        """
        self.__dbProvider.exec(sql)

    # them diem 
    def insert(self, sc: ScoreDot):
        sql = """
            INSERT INTO Scores(StudentID, SubjectID, Score1, Score2)
            VALUES (%s, %s, %s, %s)
        """
        params = (sc.StudentID, sc.SubjectID, sc.Score1, sc.Score2)
        return self.__dbProvider.exec(sql, params)

    # sua diem

    def update(self, sc: ScoreDot):
        sql = """
            UPDATE Scores
            SET 
                Score1 = %s,
                Score2 = %s
            WHERE StudentID = %s and SubjectID = %s
        """
        params = (sc.Score1, sc.Score2, sc.StudentID, sc.SubjectID)
        return self.__dbProvider.exec(sql,params)

    # lay nhieu ban ghi
    def get(self):
        sql = """
            SELECT * FROM Scores
        """
        scores = self.__dbProvider.get(sql)
        scoreDots = list(map(lambda sc:ScoreDot(sc[0], sc[1], sc[2], sc[3]), scores))
        return scoreDots

    #lay 1 ban gh
    def getOne(self, studentID: str, subjectID: str):
        sql = """
            SELECT * FROM Scores
            WHERE StudentID = %s AND subjectID = %s
        """
        params = (studentID, subjectID,)
        score = self.__dbProvider.getOne(sql, params)
        scoreDot = ScoreDot(score[0], score[1], score[2], score[3])
        return scoreDot

    # tra cuu diem thi
    def search(self, text: str):
        sql = """
            SELECT * FROM Scores
            WHERE StudentID = %s OR SubjectID = %s       
        """
        params = (text, text)
        scores = self.__dbProvider.get(sql, params)
        scoreDots = list(map(lambda sc: ScoreDot(sc[0], sc[1], sc[2], sc[3]),scores))
        return scoreDots

    # kiem tra su ton tai hoc vien
    def checkExistsStudent(self, studentID: str):
        isExists = False
        sql = """
            SELECT * FROM Scores
            WHERE StudentID = %s
        """
        params = (studentID,)
        student = self.__dbProvider.getOne(sql, params)
        if student is not None:
            isExists = True # Set thành có tồn tại
        return isExists

    def checkExistsSubject(self, subjectID: str):
        isExists = False
        sql = """
            SELECT * FROM Scores
            WHERE SubjectID = %s
        """
        params = (subjectID,)
        subject = self.__dbProvider.getOne(sql, params)
        if subject is not None:
            isExists = True # Set thành có tồn tại
        return isExists

    def xuat(self, rank =''):
        sql = """
            WITH sub AS (
                SELECT st.`StudentID`, st.`FullName`, st.`Birthday`, 
                    CASE
                        WHEN st.`sex` = 0 THEN "Nữ"
                        ELSE "Nam" 
                    END AS "Sex", 
                    st.`Place`,
                    st.`Phone`, st.`Email`, sbj.`SubName`,
                    round(((sc.`score1` + sc.`score2`*2)/3),2) as `Finalscore`
                FROM `students` st
                INNER JOIN `scores` sc
                ON st.`StudentID` = sc.StudentID
                INNER JOIN `subjects` sbj
                ON sc.`SubjectID` = sbj.`SubjectID`
            )
            SELECT *,
                CASE
                    WHEN `Finalscore` <=100 AND `Finalscore` >= 90 THEN "A"
                    WHEN `Finalscore` >= 70 THEN "B"
                    WHEN `Finalscore` >= 50 THEN "C"
                    ELSE "D" 
                END AS "Rank"
            FROM sub
        """
        
        if rank == 'A':
            sql += 'WHERE `Finalscore` <=100 AND `Finalscore` >= 90'
        elif rank == 'B':
            sql += 'WHERE `Finalscore` >= 70 AND `Finalscore` < 90'
        elif rank == 'C':
            sql += 'WHERE `Finalscore` >= 50 AND `Finalscore` < 70'
        elif rank == 'D':        
            sql += 'WHERE `Finalscore` < 50 AND `Finalscore` >= 0'
        print(sql)
        scoreExports = self.__dbProvider.get(sql)
        print(scoreExports)
        # TODO Cast tuple to ScoreExportDot
        scoreExportDots = list(map(lambda sce:ScoreExportDot(sce[0], sce[1], sce[2], sce[3], sce[4], sce[5], sce[6], sce[7], sce[8]), scoreExports))
        return scoreExportDots
        
       

        

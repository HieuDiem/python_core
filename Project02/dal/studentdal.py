
from dot import StudentDot
from  .dbprovider import DBProvider
class StudentDAL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

#tao bang neu chua ton tai
    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Students(
                StudentID Varchar(6) PRIMARY KEY,
                FullName Varchar(30) NOT NULL,
                Birthday Varchar(30) NOT NULL,
                Sex TINYINT NOT NULL,
                Place Varchar(500),
                Phone Varchar(11) NOT NULL,
                Email Varchar(100) NOT NULL
            )
        """
        self.__dbProvider.exec(sql)

# them hoc vien
    def insert(self, st: StudentDot):
        sql = """
            INSERT INTO Students(StudentID, FullName, Birthday, Sex, Place,  Phone, Email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (st.StudentID, st.FullName, st.Birthday, st.Sex, st.Place, st.Phone, st.Email)
        return self.__dbProvider.exec(sql, params)

# sua thong tin hoc vien
    def update(self, st: StudentDot):
        sql = """
            UPDATE Students
            SET
                FullName = %s,
                Birthday = %s,
                Sex = %s,
                Place = %s,
                Phone = %s,
                Email = %s
            WHERE StudentID = %s
        """
        params = (st.FullName, st.Birthday, st.Sex, st.Place, st.Phone, st.Email,st.StudentID)
        return self.__dbProvider.exec(sql, params)

# xoa hoc vien
    def delete(self, studentID: str):
        sql = """
            DELETE FROM Students
            WHERE StudentID = %s
        """
        params = (studentID,)
        return self.__dbProvider.exec(sql, params)

# lay nhieu ban ghi7
    def get(self):
        sql = """
            SELECT * FROM Students
        """
        students = self.__dbProvider.get(sql)
        # chuyen du lieu list<tuple> sang dang tui dung list<StudentDot>
        studentDots = list(map(lambda st: StudentDot(st[0], st[1], st[2], st[3], st[4], st[5], st[6]), students))
        return studentDots
# lay 1 ban ghi
    def getOne(self, studentID: str):
        sql = """
            SELECT * FROM Students
            WHERE studentID = %s
        """
        params = (studentID,)
        student = self.__dbProvider.getOne(sql, params)
        studentDot = StudentDot(student[0],
                                student[1],
                                student[2],
                                student[3],
                                student[4],
                                student[5],
                                student[6])
        return studentDot
# tim kiem
    def search(self, text: str): 
        sql = """
            SELECT * FROM Students
            WHERE 
                StudentID = %s
                OR FullName LIKE %s
                OR Email LIKE %s
        """
        params = (text, f'%{text}%', f'%{text}%')
        students = self.__dbProvider.get(sql, params)
        # chuyen du lieu list<tuple> sang dang tui dung list<StudentDot>
        studentDots = list(map(lambda st: StudentDot(st[0], st[1], st[2], st[3], st[4], st[5], st[6]), students))
        return studentDots

# kiem tr su ton tai
    def checkExists(self, studentID: str):
        isExists = False
        sql = """
            SELECT * FROM Students
            WHERE StudentID = %s
        """
        params = (studentID,)
        student = self.__dbProvider.getOne(sql, params)
        if student is not None:
            isExists = True # Set thành có tồn tại
        return isExists
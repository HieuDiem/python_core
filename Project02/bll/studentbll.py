
from dot import StudentDot

from dal import StudentDAL

class StudentBLL:
    def __init__(self):
        self.__stDAL = StudentDAL()


    def insert(self, st: StudentDot):
        return self.__stDAL.insert(st)

    def update(self, st: StudentDot):
        return self.__stDAL.update(st)

    def delete(self, studentID: str):
        return self.__stDAL.delete(studentID)

    def get(self):
        return self.__stDAL.get()

    def getOne(self, studentID: str):
        return self.__stDAL.getOne(studentID)

    def search(self, text:str):
        return self.__stDAL.search(text)

    def checkExists(self, StudentID: str):
        return self.__stDAL.checkExists(StudentID)
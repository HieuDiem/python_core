from dot import ScoreDot
from dal import ScoreDAL

class ScoreBLL:
    def __init__(self):
        self.__scDAL = ScoreDAL()

    def insert(self, sc:ScoreDot):
        return self.__scDAL.insert(sc)

    def update(self, sc:ScoreDot):
        return self.__scDAL.update(sc)

    def get(self):
        return self.__scDAL.get()

    def getOne(self, StudentID: str, SubjectID: str):
        return self.__scDAL.getOne(StudentID, SubjectID)

    def search(self, text:str):
        return self.__scDAL.search(text)

    def checkExistsStudentID(self, StudentID: str):
        return self.__scDAL.checkExistsStudent(StudentID)

    def xuat(self, rank = ''):
        return self.__scDAL.xuat(rank)

    def checkExistsSubjectID(self, SubjectID: str):
        return self.__scDAL.checkExistsSubject(SubjectID)
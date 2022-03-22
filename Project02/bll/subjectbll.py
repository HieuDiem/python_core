from dot import SubjectDot
from dal import SubjectDAL

class SubjectBLL:
    def __init__(self):
        self.__sbjDAL = SubjectDAL()

    def insert(self, sbj: SubjectDot):
        return self.__sbjDAL.insert(sbj)

    def update(self, sbj: SubjectDot):
        return self.__sbjDAL.update(sbj)

    def delete(self, SubjectID: str):
        return self.__sbjDAL.delete(SubjectID)

    def get(self):
        return self.__sbjDAL.get()

    def getOne(self, SubjectID: str):
        return self.__sbjDAL.getOne(SubjectID)

    def search(self, text:str):
        return self.__sbjDAL.search(text)

    def checkExists(self, SubjectID: str):
        return self.__sbjDAL.checkExists(SubjectID)
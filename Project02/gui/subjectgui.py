
from utils import clearScreen
from dot import SubjectDot
from bll import SubjectBLL
from tabulate import tabulate

class SubjectGUI:
    def __init__(self):
        self.__sbjBLL = SubjectBLL()

    def insertSubjectScreen(self):
        clearScreen()
        print('*** THEM MON HOC ***')
        try:
            while True:
                SubjectID = input('ma mon hoc: ')
                if SubjectID == '':
                    print('khong duoc de trong')
                    continue
                if len(SubjectID) != 6:
                    print('ma mon hoc phai bao gom 6 ktu')
                    continue
                isExists = self.__sbjBLL.checkExists(SubjectID)
                if isExists == True:
                    print('dung ma khac')
                    continue
                break

            while True:
                subName = input('ten mon hoc: ')
                if subName =='':
                    print('phai nhap ten mon hoc')
                    continue
                break

            newSubjectDot = SubjectDot(SubjectID, subName)
            count = self.__sbjBLL.insert(newSubjectDot)
            if count == 0:
                print('fail')
            else:
                print('success')

            ques = input('Nhap Y/y de tiep tuc: ')
            if ques.lower() == 'y':
                # bat dau nhap tu dau
                self.insertSubjectScreen()
        except Exception as e:
            print(e)
        finally:
            print('end')

    def updateSubjectScreen(self):
        clearScreen()
        print('*** SUA THONG TIN MON HOC ***')
        try:
            while True:
                SubjectID = input('ma mon hoc: ')
                if SubjectID == '':
                    print('khong duoc de trong')
                    continue
                if len(SubjectID) != 6:
                    print('ma mon hoc phai bao gom 6 ktu')
                    continue
                isExists = self.__sbjBLL.checkExists(SubjectID)
                if isExists == False: #True:
                    print('ko ton tai mon hoc, dung ma khac')
                    continue
                break

            while True:
                subName = input('ten mon hoc: ')
                if subName =='':
                    print('phai nhap ten mon hoc')
                    continue
                break
            #cho du lieu vao tui dung

            newSubjectDot = SubjectDot(SubjectID, subName)
            count = self.__sbjBLL.update(newSubjectDot)
            if count == 0:
                print('fail')
            else:
                print('success')

            ques = input('Nhap Y/y de tiep tuc: ')
            if ques.lower() == 'y':
                # bat dau nhap tu dau
                self.updateSubjectScreen()
        except Exception as e:
            print(e)
        finally:
            print('end')

    def deleteSubjectScreen(self):
        clearScreen()
        print('*** XOA DANH SACH MON HOC ***')
        try:
            while True:
                subjectID = input('ma mon hoc: ')
                if subjectID == '':
                    print('khong duoc de trong')
                    continue
                if len(subjectID) != 6:
                    print('ma mon hoc phai bao gom 6 ktu')
                    continue
                break
            
            isExists = self.__sbjBLL.checkExists(subjectID)
            if isExists == False:
                print('ko ton tai mon hoc')
            else:
                count = self.__sbjBLL.delete(subjectID)
                if count == 0:
                    print('fail')
                else:
                    print('success', subjectID)
            
            ques = input('Nhap Y/y de tiep tuc: ')
            if ques.lower() == 'y':
                # bat dau nhap tu dau
                self.deleteSubjectScreen()
        except Exception as e:
            print(e)
        finally:
            print('end')
    
    def searchSubjectScreen(self):
        allSubjects = self.__sbjBLL.get()
        self.printSubjects(allSubjects)
        try:
            while True:
                text = input('Nhap noi dung tim kiem: ')
                if text == '':
                    self.printSubjects(allSubjects)
                else:
                    subjectsFiltered = self.__sbjBLL.search(text)
                    self.printSubjects(subjectsFiltered)
                
                ques = input('Nhap Y/y de tiep tuc: ')
                if ques.lower() != 'y':
                    break
        except Exception as e:
            print(e)
        finally:
            print('end')

    def printSubjects(self, subjects: list):
        clearScreen()
        print(subjects)
        # print('Ma Mon hoc\tTen Mon hoc')
        # print('-'*50)
        # for sbj in subjects:
        #     print(f"{sbj.SubjectID}\t{sbj.SubName}\n")
        subjectlist = list(map(lambda sbj: [sbj.SubjectID, sbj.SubName], subjects))
        print(tabulate(subjectlist, headers=['Ma Mon Hoc', 'Ten mon Hoc'], tablefmt='psql')) 
            

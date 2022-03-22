
from utils import clearScreen
from dot import ScoreDot
from bll import ScoreBLL, StudentBLL, SubjectBLL
from tabulate import tabulate
import pandas as pd

class ScoreGUI:
    def __init__(self):
        self.__scBLL = ScoreBLL()
        self.__stBLL = StudentBLL()
        self.__sbjBLL = SubjectBLL()
    def insertScoreScreen(self):
    
        clearScreen()
        print('*** THEM DIEM THI ***')
        try:

            while True:
                studentID = input('ma hoc vien: ')
                if studentID == '':
                    print('khong duoc de trong')
                    continue
                if len(studentID) != 6:
                    print('ma hoc vien phai bao gom 6 ktu')
                    continue
                isExists = self.__stBLL.checkExists(studentID)
                if isExists == False:
                    print('chua ton tai hv')
                    continue
                break

            while True:
                subjectID = input('ma mon hoc: ')
                if subjectID == '':
                    print('khong duoc de trong')
                    continue
                if len(subjectID) != 6:
                    print('ma mon hoc phai bao gom 6 ktu')
                    continue
                isExists = self.__sbjBLL.checkExists(subjectID)
                if isExists == False:
                    print('chua ton tai mon hoc')
                    continue
                break

            isExists1 = self.__scBLL.checkExistsStudentID(studentID)
            isExists2 = self.__scBLL.checkExistsSubjectID(subjectID)
            if isExists1 == True and isExists2 == True:
                print('ton tai hoc vien va mon hoc')
            else:
                while True:
                    score1 = input('Diem qua trinh: ')
                    if score1 != '':
                        if score1.isdigit() == False:
                            print('hay nhap so')
                            continue
                        if int(score1) > 100 or int(score1) < 0:
                            print('hay nhap diem tuw 0-100')
                            continue
                    break

                while True:
                    score2 = input('Diem ket thuc: ')
                    if score2 != '':
                        if score2.isdigit() == False:
                            print('hay nhap so')
                            continue
                        if int(score2) > 100 or int(score2) < 0:
                            print('hay nhap diem tu 0-100')
                            continue
                    break

                newScreDot = ScoreDot(studentID, subjectID, score1, score2)
                count = self.__scBLL.insert(newScreDot)
                if count == 0:
                    print('fail')
                else:
                    print('success')

                ques = input('Nhap Y/y de tiep tuc: ')
                if ques.lower() == 'y':
                    # bat dau nhap tu dau
                    self.insertScoreScreen()
        except Exception as e:
            print(e)
        finally:
            print('end')
                

        # sua diem 
    def updateScoreScreen(self):
        clearScreen()
        print('*** SUA DIEM THI ***')
        try:

            while True:
                studentID = input('ma hoc vien: ')
                if studentID == '':
                    print('khong duoc de trong')
                    continue
                if len(studentID) != 6:
                    print('ma hoc vien phai bao gom 6 ktu')
                    continue
                isExists = self.__stBLL.checkExists(studentID)
                if isExists == False:
                    print('chua ton tai hv')
                    continue
                break

            while True:
                subjectID = input('ma mon hoc: ')
                if subjectID == '':
                    print('khong duoc de trong')
                    continue
                if len(subjectID) != 6:
                    print('ma mon hoc phai bao gom 6 ktu')
                    continue
                isExists = self.__sbjBLL.checkExists(subjectID)
                if isExists == False:
                    print('chua ton tai mon hoc')
                    continue
                break

            isExists1 = self.__scBLL.checkExistsStudentID(studentID)
            isExists2 = self.__scBLL.checkExistsSubjectID(subjectID)
            if isExists1 == False or isExists2 == False:
                print('khong ton tai hoc vien va mon hoc')
            else:
                while True:
                    score1 = input('Diem qua trinh: ')
                    if score1 != '':
                        if score1.isdigit() == False:
                            print('hay nhap so')
                            continue
                        if int(score1) > 100 or int(score1) < 0:
                            print('hay nhap diem tuw 0-100')
                            continue
                    break

                while True:
                    score2 = input('Diem ket thuc: ')
                    if score2 != '':
                        if score2.isdigit() == False:
                            print('hay nhap so')
                            continue
                        if int(score2) > 100 or int(score2) < 0:
                            print('hay nhap diem tu 0-100')
                            continue
                    break

                newScoreDot = ScoreDot(studentID, subjectID, score1, score2)
                count = self.__scBLL.update(newScoreDot)
                if count == 0:
                    print('fail')
                else:
                    print('success')

            ques = input('Nhap Y/y de tiep tuc: ')
            if ques.lower() == 'y':
                # bat dau nhap tu dau
                self.updateScoreScreen()
        except Exception as e:
            print(e)
        finally:
            print('end')


    def searchScoreScreen(self):
        allScores = self.__scBLL.get()
        self.printScores(allScores)
        try:
            while True:
                text = input('Nhap noi dung tim kiem: ')
                if text == '':
                    self.printScores(allScores)
                else:
                    scoresFltered = self.__scBLL.search(text)
                    self.printScores(scoresFltered)

                ques = input('Nhap Y/y de tiep tuc: ')
                if ques.lower() != 'y':
                    break
        except Exception as e:
            print(e)
        finally:
            print('end')

    def printScores(self, scores: list):
        clearScreen()
        
        # print('Ma MonHoc\Mon Hoc\Score1\Score2\Diem TK')
        # print('--------------------------------------------------')
       
        for sc in scores:
            score1 = int(sc.Score1)
            score2 = int(sc.Score2)
            finalScore = self.getFinalScore(score1, score2)
            # print(f"{sc.StudentID}\t{sc.SubjectID}\t{sc.Score1}\t{sc.Score2}\t{finalScore}")
            scorelist = list(map(lambda sc: [sc.StudentID, sc.SubjectID, sc.Score1, sc.Score2, finalScore], scores))
        print(tabulate(scorelist, headers=['Ma Hoc Vien', 'Ma Mon Hoc', 'Score1', 'Score2', 'Diem TK'], tablefmt='psql'))

    def getFinalScore(self, score1: int, score2: int):
        finalScore = int((score1 + score2*2) / 3)
        aliasScore = 'N/A'
        if (finalScore >= 90 and finalScore <= 100):
            aliasScore = 'A'
        elif (finalScore >= 70):
            aliasScore = 'B'
        elif (finalScore >= 50):
            aliasScore = 'C'
        elif (finalScore >= 0):
            aliasScore = 'D'
        return aliasScore

    def exportScoreScreen(self, rank=''):
        clearScreen()
        print('*** XUAT THONG TIN TONG HOP ***')
        data = self.__scBLL.xuat(rank) # data: list<ScoreExportDto>
        data = list(map(lambda x: [x.StudentID, x.FullName, x.FullName,x.Birthday, x.Sex, x.Place, x.Phone, x.Email, x.SubjectName, x.Finalscore, x.Rank], data)) # TODO Truy cập các giá trị kiểu ScoreExportDto
        df = pd.DataFrame(data, columns = ["StudentID", "Fullname", "Birthday", "Sex", "Place", "Phone", "Email", "SubjectName", "Finalscore", "Rank"])
        df.to_csv(f'out\out{rank}.csv', sep=',', index=False)
        print('da xuat thanh cong')
from email import header
from utils import clearScreen
from dot import StudentDot
from bll import StudentBLL
import re
from  datetime import datetime
from tabulate import tabulate

class StudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()

    def insertStudentScreen(self):
        clearScreen()
        print('*** THEM MOI HOC VIEN ***')
        while True:
            studentID = input('ma hoc vien: ')
            if studentID == '':
                print('khong duoc de trong')
                continue
            if len(studentID) != 6:
                print('ma hoc vien phai bao gom 6 ktu')
                continue
            isExists = self.__stBLL.checkExists(studentID)
            if isExists == True:
                print('dung ma khac')
                continue
            break

        while True:
            fullName = input('Ho ten: ')
            if fullName =='':
                print('phai nhap ho ten')
                continue
            break

        #bat loi ko bo trong va phai nhap dd/mm/yyy
        while True:
            birthDay = input('ngay sinh(dd/mm/yyyy): ')
            if birthDay == '':
                print('hay nhap ngay sinh')
                continue

            try:
                d = datetime.strptime(birthDay, "%d/%m/%Y")
            except:
                print('hay nhap dung dinh dang')
                continue
            break

        #ko bo trong va 0/1
        while True:
            sex = input('Gioi tinh (0-nu/1-nam): ')
            if sex == '':
                print('hay nhap gioi tinh')
                continue
            if sex != '0' and sex != '1': # if sex not in ['0', '1']
                print('hay nhap lai gioi tinh cho dung  ')
                continue
            break

        address = input('Dia chi: ') #ko phai xu ly

        # ko nhap cung dc nhung nhap theo format of phone:chi chua so, len 10-11
        while True:
            phone = input('nhap so dien thoai: ')
            if phone != '':
                if phone.isdigit() == False:
                    print('hay nhap so')
                    continue
                if len(phone) != 10 and len(phone)!= 11:
                    print('nhap 10 hoac 11 so')
                    continue
            break

        #ko nhap cung dc nhung nhap phai theo format email:xxx@xxx.xxx(x chi chu thuong or so)
        while True:
            email = input('Email: ')
            if email != '':
                emailRegex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if not re.search(emailRegex, email):
                    print('nhap lai cho dung dinh dang')
                    continue
            break
        
        #cho du lieu nhan tu ban phim vao tui dung
        newStudentDot =  StudentDot(studentID,
                                    fullName,
                                    birthDay,
                                    sex,
                                    address,
                                    phone,
                                    email)
        count = self.__stBLL.insert(newStudentDot)
        if count == 0:
            print('that bai')

        else:
            print('thanh cong')
        
        ques = input('Nhap Y/y de tiep tuc: ')
        if ques.lower() == 'y':
            # bat dau nhap tu dau
            self.insertStudentScreen()



    def updateStudentScreen(self):
        clearScreen()
        print('*** SUA THONG TIN HOC VIEN ***')
        while True:
            studentID = input('ma hoc vien: ')
            if studentID == '':
                print('khong duoc de trong')
                continue
            if len(studentID) != 6:
                print('ma hoc vien phai bao gom 6 ktu')
                continue
            isExists = self.__stBLL.checkExists(studentID)
            print(isExists)
            if isExists == False:
                print('dung ma khac')
                continue
            break

        while True:
            fullName = input('Ho ten: ')
            if fullName =='':
                print('phai nhap ho ten')
                continue
            break

        #bat loi ko bo trong va phai nhap dd/mm/yyy
        while True:
            birthDay = input('ngay sinh(dd/mm/yyyy): ')
            if birthDay == '':
                print('hay nhap ngay sinh')
                continue

            try:
                d = datetime.strptime(birthDay, "%d/%m/%Y")
            except:
                print('hay nhap dung dinh dang')
                continue
            break

        #ko bo trong va 0/1
        while True:
            sex = input('Gioi tinh (0-nu/1-nam): ')
            if sex == '':
                print('hay nhap gioi tinh')
                continue
            if sex != '0' and sex != '1': # if sex not in ['0', '1']
                print('hay nhap lai gioi tinh cho dung  ')
                continue
            break

        address = input('Dia chi: ') #ko phai xu ly

        # ko nhap cung dc nhung nhap theo format of phone:chi chua so, len 10-11
        while True:
            phone = input('nhap so dien thoai: ')
            if phone != '':
                if phone.isdigit() == False:
                    print('hay nhap so')
                    continue
                if len(phone) != 10 and len(phone)!= 11:
                    print('nhap 10 hoac 11 so')
                    continue
            break

        #ko nhap cung dc nhung nhap phai theo format email:xxx@xxx.xxx(x chi chu thuong or so)
        while True:
            email = input('Email: ')
            if email != '':
                emailRegex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                if not re.search(emailRegex, email):
                    print('nhap lai cho dung dinh dang')
                    continue
            break

        #cho du lieu nhan tu ban phim vao tui dung
        newStudentDot =  StudentDot(studentID,
                                    fullName,
                                    birthDay,
                                    sex,
                                    address,
                                    phone,
                                    email)
        count = self.__stBLL.update(newStudentDot)
        if count == 0:
            print('that bai')

        else:
            print('thanh cong')
        
        ques = input('Nhap Y/y de tiep tuc: ')
        if ques.lower() == 'y':
            # bat dau nhap tu dau
            self.updateStudentScreen()

    def deleteStudentScreen(self):
        clearScreen()
        print('*** XOA HOC VIEN ***')
        while True:
            studentID = input('ma hoc vien: ')
            if studentID == '':
                print('khong duoc de trong')
                continue
            if len(studentID) != 6:
                print('ma hoc vien phai bao gom 6 ktu')
                continue
            
            break

        isExists = self.__stBLL.checkExists(studentID)
        if isExists == False:
            print('ko ton tai hv')
        else:
            count = self.__stBLL.delete(studentID)
            if count == 0:
                print('that bai')
            else:
                print('da xoa thanh cong', studentID)
                
        ques = input('Nhap Y/y de tiep tuc: ')
        if ques.lower() == 'y':
            # bat dau nhap tu dau
            self.deleteStudentScreen()


    def searchStudentScreen(self):
        allStudents = self.__stBLL.get()
        self.printStudents(allStudents)

        while True:
            text = input('Nhap noi dung tim kiem: ')
            if text == '':
                self.printStudents(allStudents)
            else:
                studentsFiltered = self.__stBLL.search(text)
                self.printStudents(studentsFiltered)
            
            ques = input('Nhap Y/y de tiep tuc: ')
            if ques.lower() != 'y':
                break
            
    

    def printStudents(self, students: list):
        clearScreen()
        print(students)
        # print('Ma HV\t\tHo ten\t\tNgay sinh\tGioi tinh\tDia chi\t\tDien Thoai\tEmail')
        # print('-'*50)
        # for st in students:
        #     sex ='N/A'
        #     if st.Sex == 0:
        #         sex = 'Nu'
        #     elif st.Sex == 1:
        #         sex = 'Nam'
        #     print(f"{st.StudentID}\t{st.FullName}\t{st.Birthday}\t{sex}\t{st.Place}\t{st.Phone}\t{st.Email}\n")

    #TODO sd tabulate
        def aliasSex(s: dict):
            s.Sex = 'Nu' if s.Sex== 0 else 'Nam'
            return s
        student = map(aliasSex, students)
        studentlist = list(map(lambda st: [st.StudentID, st.FullName, st.Birthday, st.Sex, st.Place, st.Phone, st.Email], student))
        print(tabulate(studentlist, headers=['Ma Hoc Vien', 'Ten Hoc Vien', 'Ngay Sinh', 'Gioi Tinh', 'Dia Diem', 'So DT', 'Email'], tablefmt='psql'))

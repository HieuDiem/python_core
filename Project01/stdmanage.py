'''cac man hinh qly hoc vien'''
from utils import clearScreen
from dbprovider import readStudents, writeStudent, writeStudents
from datetime import datetime
import re

def addStudentScreen():
    clearScreen()
    print('*** THEM MOI HOC VIEN ***')
    while True:
        stID = input('ma hoc vien: ')
        if stID == '':
            print('khong duoc de trong')
            continue
        if len(stID) != 6:
            print('ma hoc vien phai bao gom 6 ktu')
            continue
        isExists = checkEixistsStudentID(stID)
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

    newStudent = {
        'ID': stID,
        'FullName': fullName,
        'Birthday': birthDay,
        'Sex': int(sex),
        'Address': address,
        'Phone': phone,
        'Email': email
    }
    writeStudent(newStudent)
    print('success:', fullName)

    ques = input('Nhap Y/y de tiep tuc: ')
    if ques.lower() == 'y':
        # bat dau nhap tu dau
        addStudentScreen()

def checkEixistsStudentID(stID: str):
    isExists = False # trang thai mac dinh la ko ton tai
    allStudents= readStudents()
    for st in allStudents:
        if st['ID'] == stID:
            isExists = True # dang ton tai
            break
    return isExists

def editStudentScreen():
    clearScreen()

    print('*** CHINH SUA THONG TIN HOC VIEN ***')
    while True:
        stID = input('ma hoc vien: ')
        if stID == '':
            print('khong duoc de trong')
            continue
        if len(stID) != 6:
            print('ma hoc vien phai bao gom 6 ktu')
            continue
        break
    
    isExists = checkEixistsStudentID(stID)
    if isExists == False:
        print('ko ton tai hoc vien')
    else:
        #TODO Advance:chon truong in nao muon sua
        while True:
            fullName = input('Ho ten: ')
            if fullName =='':
                print('phai nhap ho ten')
                continue
            break

        #tuong tu sdt, ngay sinh...
        while True:
            birthDay = input('ngay sinh(dd/mm/yyyy): ')
            if birthDay == '':
                print('hay nhap ngay sinh')
                continue
            break


        #ko bo trong va 0/1
        sex = input('Gioi tinh (0-nu/1-nam): ')
        address = input('Dia chi: ') #ko phai xu ly

        # ko nhap cung dc nhung nhap theo format of phone:chi chua so, len 10-11
        phone = input('so dien thoi: ') 

        #ko nhap cung dc nhung nhap phai theo format email:xxx@xxx.xxx(x chi chu thuong or so)
        email = input('Email: ')

        allStudents = readStudents()
        for st in allStudents:
            if st['ID'] == stID:
                st['FullName'] = fullName
                st['Birthday'] = birthDay
                st['Sex'] = int(sex)
                st['Address'] = address
                st['Phone'] = phone
                st['Email'] = email
                break
        writeStudents(allStudents)
        print('da chinh sua thanh cong hoc vien ', fullName)

    ques = input('Nhap Y/y de tiep tuc: ')
    if ques.lower() == 'y':
    # bat dau nhap tu dau
        editStudentScreen()

def removeStudentScreen():
    clearScreen()
    print('*** XOA HOC VIEN ***')
    while True:
        stID = input('ma hoc vien: ')
        if stID == '':
            print('khong duoc de trong')
            continue
        if len(stID) != 6:
            print('ma hoc vien phai bao gom 6 ktu')
            continue
        
        break
        #remove student by ID
    
    isExists = checkEixistsStudentID(stID)
    if isExists == False:
        print('hoc vien ko ton tai')
    else:
        allStudents = readStudents()
        newAllStudents = []
        for st in allStudents:
            if st['ID'] != stID:
                newAllStudents.append(st)
        writeStudents(newAllStudents)
        print('da xoa hoc vien co ma: ', stID)

    ques = input('Nhap Y/y de tiep tuc: ')
    if ques.lower() == 'y':
        # bat dau nhap tu dau
        removeStudentScreen()

def searchStudentScreen():
    clearScreen()

    print('*** DANH SACH HOC VIEN ***')
    allStudents = readStudents()
    printStudents(allStudents)

    while True:
        searchContent = input('Nhap noi dung tim kiem: ')
        if searchContent == '':
            print(allStudents)
        else:
            studentsFiltered = []
            for st in allStudents:
                if st['ID'] == searchContent\
                    or searchContent.lower() in st['FullName']\
                        or searchContent.lower() in st['Email']:
                    studentsFiltered.append(st)

            printStudents(studentsFiltered)
        
        ques = input('Nhap Y/y de tiep tuc: ')
        if ques.lower() != 'y':
            break
        # bat dau nhap tu dau
        # addStudentScreen()

def printStudents(students: list):
    print('Ma HV\t\tHo ten\t\tNgay sinh\tGioi tinh\tDia chi\t\tDien Thoai\tEmail')
    print('-'*50)
    for st in students:
        sex =''
        if st['Sex'] == '0':
            sex = 'Nu'
        elif st['Sex'] == '1':
            sex = 'Nam'
        print(f"{st['ID']}\t{st['FullName']}\t{st['Birthday']}\t{st['Sex']}\t{st['Address']}\t{st['Phone']}\t{st['Email']}\n")









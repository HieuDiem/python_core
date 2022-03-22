from utils import clearScreen, printMenu
from gui import StudentGUI, SubjectGUI, ScoreGUI
from tabulate import tabulate

class MainGUI:
    def __init__(self):
        self.__stGUI = StudentGUI()
        self.__sbjGUI = SubjectGUI()
        self.__scGUI = ScoreGUI()

    def mainMenuScreen(self):
        
        # Xoá trắng màn hình
        clearScreen()

        print('*** MENU CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI ***')
        funcs = [
            '[1] Quản lý Học viên',
            '[2] Quản lý Môn học',
            '[3] Quản lý Điểm thi',
            '[4] IN KET QUA',
            '[0] Thoát'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4','0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            # Hiển thị màn hình QL Học viên
            self.studentMenuScreen()
        elif cmd == '2':
            # Hiển thị màn hình QL Môn học
            self.subjectMenuScreen()
        elif cmd == '3':
            # Hiển thị màn hình QL Điểm thi
            self.scoreMenuScreen()
        elif cmd == '4':
            self.printTotal()
        elif cmd == '0':
            exit()


    def studentMenuScreen(self):
        clearScreen()

        print('*** QUẢN LÝ HỌC VIÊN ***')
        funcs = [
            '[1] Thêm',
            '[2] Sửa',
            '[3] Xoá',
            '[4] Tìm kiếm',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__stGUI.insertStudentScreen()
            # Nhập xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '2':
            self.__stGUI.updateStudentScreen()
            # Sửa xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '3':
            self.__stGUI.deleteStudentScreen()
            # Xoá xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '4':
            self.__stGUI.searchStudentScreen()
            # Tìm kiếm xong thì quay lại màn hình studentMenuScreen
            self.studentMenuScreen()
        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()

    
    def subjectMenuScreen(self):
        clearScreen()

        print('*** QUẢN LÝ MON HỌC  ***')
        funcs = [
            '[1] Thêm',
            '[2] Sửa',
            '[3] Xoá',
            '[4] Tìm kiếm',
            '[0] Quay lại'
        ]
        printMenu(funcs)

        cmd = ''
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.__sbjGUI.insertSubjectScreen()
            # Nhập xong thì quay lại màn hình studentMenuScreen
            self.subjectMenuScreen()
        elif cmd == '2':
            self.__sbjGUI.updateSubjectScreen()
            # Sửa xong thì quay lại màn hình studentMenuScreen
            self.subjectMenuScreen()
        elif cmd == '3':
            self.__sbjGUI.deleteSubjectScreen()
            # Xoá xong thì quay lại màn hình studentMenuScreen
            self.subjectMenuScreen()
        elif cmd == '4':
            self.__sbjGUI.searchSubjectScreen()
            # Tìm kiếm xong thì quay lại màn hình studentMenuScreen
            self.subjectMenuScreen()
        elif cmd == '0':
            # Quay lại màn hình Menu chính
            self.mainMenuScreen()

    def scoreMenuScreen(self): 
        clearScreen()

        print('*** QUAN LY DIEM THI *** ')
        funcs= [
            '[1] Nhap diem thi',
            '[2] Sua diem thi',
            '[3] Tra cuu diem thi',
            '[0] quay lai'
        ]
        printMenu(funcs)
        cmd =''
        while cmd not in ['1', '2', '3','0']:
            cmd = input('chon chuc nang: ')
        if cmd == '1':
            self.__scGUI.insertScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '2':
            self.__scGUI.updateScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '3':
            self.__scGUI.searchScoreScreen()  
            self.scoreMenuScreen()
        elif cmd == '0':
            self.mainMenuScreen()

    def printTotal(self):
        clearScreen()

        print('*** IN KET XUAT THONG TIN HOC VIEN***')
        funcs = [
            '[9] Xuat file tat ca cac hoc vien',
            '[1] Xuat file tat ca cac hoc vien co diem tong ket A',
            '[2] Xuat file tat ca cac hoc vien co diem tong ket B',
            '[3] Xuat file tat ca cac hoc vien co diem tong ket C',
            '[4] Xuat file tat ca cac hoc vien co diem tong ket D',
            '[0] quay lai'
        ]
        printMenu(funcs)
        
        cmd = ' '
        while cmd not in ['9', '1', '2', '3', '4', '0']:
            cmd = input('chon chuc nang')
        if cmd == '9':
            self.__scGUI.exportScoreScreen()
            self.printTotal()
        if cmd == '1':
            self.__scGUI.exportScoreScreen('A')
            self.printTotal()
        if cmd == '2':
            self.__scGUI.exportScoreScreen('B')
            self.printTotal()
        if cmd == '3':
            self.__scGUI.exportScoreScreen('B')
            self.printTotal()
        if cmd == '4':
            self.__scGUI.exportScoreScreen('D')
            self.printTotal() 
        if cmd == '0':
            self.mainMenuScreen() 


if __name__ == '__main__':
    mainGUI = MainGUI()
    mainGUI.mainMenuScreen()
    
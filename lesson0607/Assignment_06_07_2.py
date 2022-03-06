# ho ten: Nguyen Thi Diem
# lop Python02
# bai06_07_2


class Mother:
    def display(self):
        print('This is Mother')

class Child(Mother):
    def display(self):
        print('This is child')

child = Child()
child.display()
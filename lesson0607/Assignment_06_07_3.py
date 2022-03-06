# ho ten: Nguyen Thi Diem
# lop Python02
# bai06_07_3


class Animal:
    def set_value(self, name, age):
        self.Name = name
        self.Age = age

class Zebra(Animal):
    def message(self):
        print('Zebra:', self.Name, self.Age)

class Dolphin(Animal):
    def message(self):
        print('Dolphin:', self.Name, self.Age)

zebra = Zebra()
zebra.set_value('A', 5)
zebra.message()

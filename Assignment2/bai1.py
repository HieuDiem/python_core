# ho ten: Nguyen Thi Diem
# lop Python02
# bai1

a = int(input('input the first test score: '))
b = int(input('input the second test score: '))
c = int(input('input the third test score: '))
num = [a, b, c]
sum = 0
for i in num:
    sum += i
    avg = sum / len(num)
print(avg)
if avg > 95:
    print('Congratulate the user')
else:
    pass

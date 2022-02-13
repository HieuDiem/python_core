# ho ten: Nguyen Thi Diem
# lop Python02
# bai2

hours_worked = float(input('number of hours worked: '))
pay_rate = float(input('hourly pay rate: '))
hours_base = 40
overtime = 1.5

if hours_worked > hours_base:
    overtime_pay = (hours_worked - hours_base)*pay_rate*overtime
    gosspay = hours_base*pay_rate + overtime_pay
    print(overtime_pay)
    print(gosspay)
else:
    print(hours_worked*pay_rate)

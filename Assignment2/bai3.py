# ho ten: Nguyen Thi Diem
# lop Python02
# bai3

min_salary = 30000
min_years = 2

salary = float(input('nhap muc luong hang nam: '))
years_on_job = float(input('nhap so nam lam viec: '))

if salary < min_salary:
    print('You must earn at least $'+ str(min_salary) + ' per year to qualify.')
else:
    if years_on_job >= min_years:
        print('You qualify for the loan')
    else:
        print('Youmust have been on your current job for at least '+ str(min_years) +' years to qualify')
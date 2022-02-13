# ho ten: Nguyen Thi Diem
# lop Python02
# bai5

keep_going = 'y'
while keep_going == 'y':
    sales = float(input('the amount of sales: '))
    
    comm_rate = float(input('the commission rate: '))
    
    commission = sales * comm_rate

    print('the commission is '+ str(commission))
    
    keep_going = input( 'Do you want to calculate another commission? (Enter y for yes): ' )
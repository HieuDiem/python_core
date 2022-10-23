from email import header


file = open("vidu.csv", mode="r")
file_new = open("vidu_new.csv", mode="w")

header = file.readline()
print(header)
file_new.write(header.strip() + ", Diem TB, Hoc Luc\n")

row = file.readline()
while row != "":
    row_list = row.split(",")

    toan = float(row_list[2])
    van = float(row_list[3])

    tb = round((toan + van)/2, 1)

    rank = ""
    if tb >= 8.0:
        rank = "Gioi"
    elif tb >= 6.5:
        rank = "Tien Tien"
    elif tb >= 5.0:
        rank = "Trung Binh"
    else:
        rank = "Yeu"

    row_new = row.strip() + "," + str(tb) + ","+ rank + "\n"
    file_new.write(row_new)
    row = file.readline()

k = int(input("Nhap do dai doan thang: "))

s = ""
for i in range(k):
    if i % 2 == 0:
        s += "* "
    else:
        s += "$ "
print(s)
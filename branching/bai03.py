# Input
x = int(input("Nhap so nguyen: "))

# Output
# Cách 1
if x < 0:
    print("Am")
else:
    if x == 0:
        print("So khong")
    else:
        print("So duong")

# Cách 2
if x <= 0:
    if x < 0:
        print("Am")
    else:
        print("So khong")
else:
    print("So duong")

# Cách 3
if x < 0:
    print("Am")

if x == 0:
    print("So khong")

if x > 0:
    print("So duong")

# Cách 4
if x < 0:
    print("Am")
elif x == 0:
    print("So khong")
else:
    print("So duong")

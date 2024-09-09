# -1, 2, 3 => -1
# -1, 2, -3 => -4

a = int(input("Nhập số vào a: "))
b = int(input("Nhập số vào b: "))
c = int(input("Nhập số vào c: "))

# -1, 2, -3
sum = 0
if a < 0:
    sum = sum + a 

if b < 0:
    sum = sum + b 

if c < 0:
    sum = sum + c

print(sum)



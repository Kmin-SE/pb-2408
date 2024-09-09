# -1, 2, 3 => 1
# -1, 2, -3 => 2

a = int(input("Nhập số vào a: "))
b = int(input("Nhập số vào b: "))
c = int(input("Nhập số vào c: "))

count = 0
if a < 0:
    count = count + 1

if b < 0:
    count = count + 1

if c < 0:
    count = count + 1

print(count)



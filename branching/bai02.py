# Kiểm tra số nguyên x được nhập vào từ bàn phím có phải là số âm không.

# Input
a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

# Output
if a == b and b == c:
    print("Tam giac deu")
else:
    print("Tam giac khong deu")

# a = 4
# b = 2
# c = 6

# if (a + b + c) / a == 3:
#     print("Tam giac deu")
# else:
#     print("Tam giac khong deu")

# Output
# if a == b == c:
#     print("Tam giac deu")
# else:
#     print("Tam giac khong deu")

# test case

# Input
a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))

# Output
# if not(a == b and b == c):
#     print("Tam giac khong deu")
# else:
#     print("Tam giac deu")

if a != b or b != c:
    print("Tam giac khong deu")
else:
    print("Tam giac deu")

# De Morgan
# not (A and B)
# not(A) or not(B)
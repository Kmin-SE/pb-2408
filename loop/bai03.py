#Cách 1
# i chạy tuần tự từ n về 1: 
# với mỗi giá trị i thì print(i) nếu i là lẻ

# n = int(input("Nhap so nguyen: "))
# i = n
# while i >= 1:
#     if i % 2 == 1:
#         print(i)
#     i = i - 1

# Cách 2
n = int(input("Nhap so nguyen: "))
i = None
if n % 2 == 1:
    i = n
else:
    i = n-1
while i >= 1:
    print(i)
    i = i - 2





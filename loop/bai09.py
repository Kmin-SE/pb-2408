# a chia hết cho b thì b là ước của a
# n = 6 => 1 2 3 6
# n = 9 => 1 3 9

# i chạy từ 1 đến n
# Nếu i là ước của n thì in ra i

n = int(input("Nhap so nguyen: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

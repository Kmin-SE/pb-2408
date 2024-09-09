# m = 15
# n = 16
# for i in range(m, n+1):
#     if i % 6 == 0:
#         print(i)
#         break
# else:
#     print("Khong co")

def tim(m, n):
    for i in range(m, n+1):
        if i % 6 == 0:
            return i
    
    return "Khong co"

def cn_tim():
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    kq = tim(m, n)
    print(kq)

cn_tim()
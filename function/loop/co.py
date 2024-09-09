
n = 5
flag = False
for i in range(2, n):
    if n % i == 0:
        flag = True
        break

if flag == True:
    print("Yes")
else:
    print("No")

def co_uoc(n):
    flag = False
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break

    return flag

def co_uoc_2(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def cn_co_uoc():
    n = int(input("Nhap n: "))
    if co_uoc(n) == True:
        print("Yes")
    else:
        print("No")
cn_co_uoc()
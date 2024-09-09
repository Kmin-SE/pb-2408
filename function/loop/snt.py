def la_snt(n):
    # Đếm xem n có bao nhiêu ước
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    # Nếu n có đúng 2 ước thì đó SNT
    if dem == 2:
        return True
    else:
        return False
    
def la_snt_2(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
    
print(la_snt_2(16))
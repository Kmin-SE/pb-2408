# Hàm nhập mảng
def nhap_mang():
    a = []
    n = int(input(("Nhap so luong phan tu: ")))

    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    
    return a

def test_nhap_mang():
    b = nhap_mang()
    print(b)

# Hàm liệt kê số dương
def liet_ke_duong(arr):
    for e in arr:
        if e > 0:
            print(e)

def test_lk_duong():
    a = nhap_mang()
    liet_ke_duong(a)

# Đếm số lẻ
def dem_le(arr):
    dem = 0
    for e in arr:
        if e % 2 == 1:
            dem += 1
    return dem

def test_dem_le():
    a = nhap_mang()
    kq = dem_le(a)
    print(kq)

# Tổng âm
def tong_am(arr):
    tong = 0
    for e in arr:
        if e < 0:
            tong += e
    return tong

def test_tong_am():
    a = nhap_mang()
    kq = tong_am(a)
    print(kq)

test_tong_am()
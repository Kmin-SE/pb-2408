def xin_chao(ten, nam_sinh):
    print(f"Xin chào, mình tên là {ten}.")
    print(f"Mình sinh năm {nam_sinh}. ")
    print("Rất vui được gặp bạn.")
    tuoi = 2024 - nam_sinh
    return tuoi

def nhap_ten():
    name = int(input("Nhap ten: "))
    while name == "":
        name = int(input("Nhap ten: "))
    return name

def nhap_nam_sinh():
    yob = int(input("Nhap nam sinh: "))
    while yob < 1900 or yob > 2024:
        yob = int(input("Nhap nam sinh: "))
    return yob

def cn_xin_chao():
    name = nhap_ten()
    yob = nhap_nam_sinh()
    t = xin_chao(name, yob)
    print("=> Tuoi:", t)


cn_xin_chao()



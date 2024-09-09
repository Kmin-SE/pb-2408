def xin_chao(ten, nam_sinh):
    print(f"Xin chào, mình tên là {ten}.")
    print(f"Mình sinh năm {nam_sinh}. ")
    print("Rất vui được gặp bạn.")
    tuoi = 2024 - nam_sinh
    return tuoi

def cn_xin_chao():
    name = input("Nhap ten: ")
    yob = int(input("Nhap nam sinh: "))
    t = xin_chao(name, yob)
    print("=> Tuoi:", t)

cn_xin_chao()



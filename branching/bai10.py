born = int(input("Nhập năm sinh: "))
weight = float(input("Nhập cân nặng: "))
height = float(input("Nhập chiều cao: "))
age = 2024 - born
if age >= 18 :
    BMI = weight / ((height)**2)
    danh_gia = ""
    if BMI < 18.5:
       danh_gia = "Gay"
    elif  BMI < 25 :
        danh_gia = "Binh thuong"
    elif  BMI < 30 :
       danh_gia = "Thua can"
    else:
       danh_gia = "Beo phi"

    print("BMI:", BMI)
    print("Danh gia:", danh_gia)

else:
   print("Không khả dụng")      
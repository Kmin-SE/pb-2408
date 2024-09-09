
diem = float(input("Nhập điểm của bạn: "))

if diem < 5.0:
    print("Bạn không đủ điều kiện tốt nghiệp.")
else:
    print("Được tốt nghiệp")
    if diem >= 8.0:
        print("Loại giỏi.")
    elif diem >= 6.5:
        print("Loại khá.")
    else:
        print("Loại trung bình.")


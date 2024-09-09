# day = int(input("Nhập ngày cần kiểm tra: "))
# month = int (input("Nhập tháng cần kiểm tra: "))
# year = int(input("Nhập năm cần kiểm tra: "))
# if day <= 31 and month <= 12 and month != 2 :
#     print ("Ngày" , day , "Tháng" , month , "Năm" , year , "Hợp lệ")
# elif month == 2 and day <= 29:
#     print("Ngày" , day , "Tháng" , month , "Năm" , year , "Hợp lệ")
# else:
#     print("Ngày" , day , "Tháng" , month , "Năm" , year , " Không hợp lệ")  

#Nhập ngày, tháng, năm
# ngay = int(input("Ngày: "))
# thang = int(input("Thang: "))
# nam = int(input("Năm: "))


# #Kiểm tra tính hợp lệ
# if(1 <= thang <= 12 and nam > 0):
#    if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
#        if(1 <= ngay <= 31):
#            print("Hợp lệ.")
#        else:
#            print("Không hợp lệ.")
#    if(thang == 4 or thang == 6 or thang == 9 or thang == 11):
#        if(0 < ngay <= 30):
#            print("Hợp lệ")
#        else:
#            print("Không hợp lệ")
#    if(thang == 2):
#        if(nam%4==0 and nam%100!=0) or (nam%400==0):
#            if(0 < ngay <= 29):
#                print("Hợp lệ")
#            else:
#                print("Không hợp lệ")
#        else:
#            if(0 < ngay <= 28):
#                print("Hợp lệ")
#            else:
#                print("Không hợp lệ")
# else:
#    print("Không hợp lệ")


ngay = int(input("Ngày: "))
thang = int(input("Thang: "))
nam = int(input("Năm: "))


#Kiểm tra tính hợp lệ
# if(1 <= thang <= 12 and nam > 0):
#     so_ngay = None
#     if thang in [1, 3, 5, 7, 8, 10, 12]:
#         so_ngay = 31
#     elif thang in [4, 6, 9, 11]:
#         so_ngay = 30
#     else:
#         if (nam%4==0 and nam%100!=0) or (nam%400==0):
#             so_ngay = 29
#         else:
#             so_ngay = 28

#     if(0 < ngay <= so_ngay):
#            print("Hợp lệ.")
#     else:
#         print("Không hợp lệ.")
   
# else:
#    print("Không hợp lệ")


so_ngay = None
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else:
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        so_ngay = 29
    else:
        so_ngay = 28

if(1 <= thang <= 12 and nam > 0 and 0 < ngay <= so_ngay):
    print("Hợp lệ.")
else:
    print("Không hợp lệ.")

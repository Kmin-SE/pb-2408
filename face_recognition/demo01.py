import cv2
print(cv2.__version__)

# Đọc ảnh từ file
image = cv2.imread('vdbao.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_edited = cv2.add(image, 20)

# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (200, 200)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (400, 400)

# Blue color in BGR
color = (0, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Hiển thị ảnh trong cửa sổ mới
cv2.imshow('Displayed Image', image)
# cv2.imshow('Displayed Edited Image', image_edited)

# Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
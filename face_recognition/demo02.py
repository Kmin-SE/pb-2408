import cv2
import face_recognition

def fr(file_name):
    image = face_recognition.load_image_file(file_name)

    locations = face_recognition.face_locations(image)
    print(locations)
    (top, right, bottom, left) = locations[0]
    cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 3)


    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("Result", image)

    # Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
    cv2.waitKey(0)

    # Đóng cửa sổ hiển thị
    cv2.destroyAllWindows()

fr("vdbao.png")
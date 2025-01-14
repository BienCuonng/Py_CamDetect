import cv2
import numpy as np
import os

# Khởi tạo bộ nhận diện khuôn mặt
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# Font chữ để hiển thị
font = cv2.FONT_HERSHEY_COMPLEX

id = 0
# Danh sách tên người dùng
names = ['0', 'Cuong', '2', '3', '4', '5']

# Mở camera
cam = cv2.VideoCapture(0)

# Kiểm tra xem camera có mở được không
if not cam.isOpened():
    print("Không thể mở camera. Hãy kiểm tra lại kết nối.")
    exit()

cam.set(3, 640)  # Đặt chiều rộng video
cam.set(4, 480)  # Đặt chiều cao video

# Đặt kích thước tối thiểu để nhận diện khuôn mặt
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    
    if not ret:
        print("Không thể lấy khung hình từ camera. Hãy thử lại.")
        continue
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        
        if confidence < 100:
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('Nhan dien khuon mat', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:  # Nhấn ESC để thoát
        break

# Giải phóng camera và đóng các cửa sổ
cam.release()
cv2.destroyAllWindows()

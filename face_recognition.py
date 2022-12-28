import cv2

# Load tệp haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Khởi tạo webcam
webcam = cv2.VideoCapture(0)

while True:
    # Đọc hình ảnh từ webcam
    _, frame = webcam.read()

    # Chuyển đổi hình ảnh sang đen trắng
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt trong hình ảnh đen trắng
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Vẽ hình chữ nhật quanh các khuôn mặt được phát hiện
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Hiển thị hình ảnh với các hình chữ nhật được vẽ quanh các khuôn mặt
    cv2.imshow("Webcam", frame)

    # Nếu người dùng nhấn phím "q", thoát khỏi vòng lặp
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Ngắt kết nối với webcam và đóng cửa sổ hiển thị hình ảnh
webcam.release()
cv2.destroyAllWindows()











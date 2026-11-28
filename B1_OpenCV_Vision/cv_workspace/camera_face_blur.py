import cv2

# 1. 加载分类器
cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# 2. 打开电脑默认摄像头（0 代表默认摄像头）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("无法打开摄像头，请检查是否被其他软件占用！")
    exit()

print("摄像头已打开，按键盘 'q' 键退出...")

# 3. 实时处理死循环
while True:
    # 逐帧读取画面
    ret, frame = cap.read()
    if not ret:
        print("无法获取画面")
        break

    # 转灰度（检测器只认灰度）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

    # 遍历每一张脸进行打码
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face_roi, (99, 99), 0)
        frame[y:y+h, x:x+w] = blurred

    # 显示画面（窗口名字叫 Camera Test）
    cv2.imshow("Camera Test - Press Q to quit", frame)

    # 监听键盘，如果按下 'q' 键就跳出死循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
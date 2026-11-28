import cv2

# 1. 加载人脸分类器模型
cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    print("模型加载失败，请检查路径！")
    exit()

# 2. 读取原图并转为灰度图
img = cv2.imread("lena2.jpg")
if img is None:
    print("图片读取失败，请检查图片路径！")
    exit()
    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 检测人脸
# 1.1 是缩放比例，5 是最小邻居数
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print(f"共检测到 {len(faces)} 个目标")

# 4. 遍历每一个框，进行局部模糊
for (x, y, w, h) in faces:
    # 过滤掉小于 200 像素的误检框
    if w > 200 and h > 200:
        # 切片：取出局部人脸
        face_roi = img[y:y+h, x:x+w]
        # 模糊：99x99 的高斯核
        blurred = cv2.GaussianBlur(face_roi, (99, 99), 0)
        # 覆盖：写回原图
        img[y:y+h, x:x+w] = blurred
        print(f"已模糊坐标: x={x}, y={y}")


# ---------- 追加：亮度与对比度调整 ----------
print("正在调整亮度和对比度...")
alpha = 1.5   # 对比度增益（1.5 倍）
beta = 30     # 亮度增量（增加 30）

# 使用 convertScaleAbs 函数进行线性变换
adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)


# 5. 保存最终结果
output_name = "lena2_final_script.jpg"
cv2.imwrite(output_name, img)
print(f"亮度对比度调整完毕，已保存为 {output_name}")
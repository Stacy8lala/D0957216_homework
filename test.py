import cv2

# 創建攝影機對象
cap = cv2.VideoCapture(1) # 0表示預設的攝影機

# 設置攝影機的尺寸
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 檢查攝影機是否打開
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# 持續讀取視頻流，直到按下 q 鍵停止
while True:
    # 從攝影機中讀取一幀影像
    ret, frame = cap.read()

    # 檢查影像是否讀取成功
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # 顯示影像
    cv2.imshow('frame', frame)
    cv2.imwrite('photo.jpg', frame)

    # 按下 q 鍵停止
    if cv2.waitKey(1) == ord('q'):
        break

# 釋放攝影機資源
cap.release()

# 關閉所有視窗
cv2.destroyAllWindows()
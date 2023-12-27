# 이미지 파일 경로
image_path = 'convert/image (1).jpg'

import cv2
import numpy as np

# 드래그 상태를 저장할 변수
drawing = False
start_x, start_y = -1, -1

# 마우스 이벤트 핸들러 함수
def draw_line(event, x, y, flags, param):
    global start_x, start_y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img_resized, (start_x, start_y), (x, y), (0, 0, 255), 5)
            start_x, start_y = x, y

# 원본 이미지 읽기
img = cv2.imread(image_path)

# 이미지 크기 임시로 변경
img_resized = cv2.resize(img, (1000, 1000))

# 윈도우 생성 및 마우스 이벤트 설정
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_line)

while True:
    cv2.imshow("Image", img_resized)
    key = cv2.waitKey(1)

    # 's' 키를 누르면 이미지 저장
    if key == ord("s"):
        # 원본 크기로 복구
        img_restored = cv2.resize(img_resized, (img.shape[1], img.shape[0]))

        # 그린 부분 추출
        mask = np.zeros_like(img_restored)
        mask[np.where((img_restored == [0, 0, 255]).all(axis=2))] = [0, 0, 255]
        extracted_image = cv2.bitwise_and(img_restored, mask)

        # 추출된 이미지 저장
        cv2.imwrite("save.jpg", extracted_image)
        print("이미지 저장 완료!")
        break

    # 'q' 키를 누르면 종료
    if key == ord("q"):
        break

cv2.destroyAllWindows()

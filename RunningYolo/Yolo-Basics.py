from ultralytics import YOLO
import cv2
import cvzone


model = YOLO('../Yolo-weights/yolov8l.pt')
results = model('Images/1.png', show=True)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)  # width 640
# cap.set(4, 720)  # height 480
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('Image', img)
#     cv2.waitKey(1)

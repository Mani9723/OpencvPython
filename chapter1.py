import cv2

# Part 1: Read and open an image

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("output",img)
# cv2.waitKey(0)

# Part 2: Read and open video

# cap = cv2.VideoCapture("Resources/test_video.mp4")
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3,640) # Set height
cap.set(4,480) # set width
# cap.set(10,100) # set brightness

while True:
    success, img = cap.read() # default webcam, parameter >= 0 external webcam
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


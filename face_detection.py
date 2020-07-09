import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier("C:/Users/jorik/Documents/opencv-4.3.0/opencv-4.3.0/data/haarcascades/haarcascade_frontalface_default.xml")

# cv2.namedWindow("test")

# To capture video from webcam.
cam = cv2.VideoCapture(0)
while True:
    # Read the frame
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    # cv2.imshow("test", frame)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

    # Display
    cv2.imshow('img', frame)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cam.release()
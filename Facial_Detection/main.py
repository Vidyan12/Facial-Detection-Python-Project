# Import the OpenCV library
import cv2

# Load the pre-trained Haar Cascade face detector from the XML file
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Read the input image (replace 'face.jpg' with the path to your image)
img = cv2.imread('face.jpg')

# Detect faces in the image using the detectMultiScale method
# 1.1 is the scaleFactor, 4 is the minNeighbors
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)

# Loop through each detected face and draw a rectangle around it
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save the image with detected faces to a new file ('face_detected.png')
cv2.imwrite("face_detected.png", img)

# Print a success message to the console
print('Successfully saved')

from django.shortcuts import render
from .models import FaceAuth
from django.conf import settings

# Create your views here.


def face_auth_create(request):

	if request.user.is_authenticated:

		import cv2
		import time 
		# Load the cascade
		path = settings.MEDIA_ROOT + 'xml/haarcascade_frontalface_default.xml'
		face_cascade = cv2.CascadeClassifier(path)

		# To capture video from webcam. 
		cap = cv2.VideoCapture(0)
		# To use a video file as input 
		# cap = cv2.VideoCapture('filename.mp4')

		start = time.time()
		while True:
		    # Read the frame
		    _, img = cap.read()
		    # Convert to grayscale
		    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		    # Detect the faces
		    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
		    # Draw the rectangle around each face
		    for (x, y, w, h) in faces:
		        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
		    # Display
		    # cv2.imshow('img', img)
		    # Stop if escape key is pressed
		    k = cv2.waitKey(30) & 0xff

		    end = time.time()
		    print(end - start)

		    time_diff = end - start

		    if k==27:
		        break
		    if time_diff > 5 and len(faces) == 1:
		    	x, y, w, h = faces[0]
		    	cv2.imwrite('ouput.png', img[y:y+h, x:x+w])
		    	break
		# Release the VideoCapture object
		cap.release()

		

		return render(request, "face.html", {'language': language, 'face': face})


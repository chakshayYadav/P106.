import cv2


# Create our body classifier
body_cascade = cv2.CascadeClassifier('C:/Users/chaks/OneDrive/Desktop/python/C106/PRO-C106-Student-Boilerplate/haarcascade_frontalface_default.xml') 


# Initiate video capture for video file
cap = cv2.VideoCapture('C:/Users/chaks/OneDrive/Desktop/python/C106/PRO-C106-Student-Boilerplate/PRO-106-ProjectTemplate-main/walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_cascade.detectMultiScale(gray, 1.1, 5)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 32: #32 is the Space Key  
        break

cap.release()
cv2.destroyAllWindows()

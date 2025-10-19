import cv2

#train the model.
trained=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#get access to webcam/photo/video.

webcam=cv2.VideoCapture(0)

while True:
    #get the current frame

    succ, frame = webcam.read()
    
    #turn it grayshaded.

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect the faces.

    cords=trained.detectMultiScale(grayframe)

    #draw the square for visual purposes.

    for (x,y,w,h) in cords:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255, 0), 10)

    #display the webcam with the detection.

    cv2.imshow('Face Detector', frame)
    key=cv2.waitKey(1)

    #end the program.
    if key==81 or key==131:
        break
webcam.release()

print("Code Completed!")

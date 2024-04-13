import cv2

face= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#so haarcascade files are basically pattern finding like haar waves in small rectangles or pixels

eye= cv2.CascadeClassifier('haarcascade_eye.xml')

camera= cv2.VideoCapture(0)
# 0 is the index of camera

while 1 :
    ret, img = camera.read()   #order is important here ret is return from read function
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #grayscale bc i am racist and well also bc it is more accurate
    faces = face.detectMultiScale(gray,1.3,5) #gray is the image, 1.3 is how smallest rectangle should get
                                                                    #recursive cropping, min neighbour is basically rechecking
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) #draw on img, top left, bottom right, color, stroke)
        roi_gray = gray[ y:y+h,x:x+w]                     #new image for less work for eye
        roi_img = img[ y:y+h,x:x+w ]

        eyes= eye.detectMultiScale(roi_gray)

        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_img,(ex,ey),(ex+ew,ey+eh),(155,155,155),2)

    cv2.imshow('face_recognizer',img)               #window name, image to show

    k=cv2.waitKey(30) & 0xff
    if k == 27 :
        break
camera.release()
cv2.destroyAllWindows()



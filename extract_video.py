import cv2 as cv
import os

cap=cv.VideoCapture("E://openCV_images/03.mp4")

try:
    #creating a folder named extract_images
    if not os.path.exists("extract_images"):
        os.makedirs("extract_images")  
except OSError:
    print("error with create folder")
    
current_frame=0

while(True):
    ret,frame=cap.read()
    
    if ret:
        name="./extract_images/img"+str(current_frame)+".jpg"
        print(name)
        cv.imwrite(name,frame)
        current_frame+=1
    else:
        break
    
cap.release()
cv.destroyAllWindows()

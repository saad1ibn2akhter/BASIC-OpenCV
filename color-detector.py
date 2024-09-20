import cv2
import numpy as np


lower = np.array([35,50,70])
higher =  np.array([185,205,255])

video = cv2.VideoCapture(0)



print('libs are found')

while True :
    success , img = video.read()
    image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    image_rgb = cv2.cvtColor(img,  cv2.COLOR_BGR2RGBA)
    
    bordered_img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[45, 100, 200])
    mask =  cv2.inRange(image,lower,higher)
    
    cv2.rectangle(img, (50, 50), (155, 150), (0, 255, 0), thickness=2)


    cv2.imshow("mask" , mask)
    print(mask.props)

    cv2.imshow("ss", bordered_img)
    
    cv2.imshow("vidoe" , img)
    cv2.imshow("RGB"  , image_rgb)
    
    
    

    cv2.waitKey(1)
    

    

import cv2
import os
import imutils
from Human_Detection import Detector

imagesPath = "Images"
imagesPathList = os.listdir(imagesPath)

for imageName in imagesPathList:
    print('Objeto leido =', imageName)
    img = cv2.imread(imagesPath + '/' + imageName)
    img = imutils.resize(img, width=650) #650
    img = Detector(img)
    #cv2.imshow('Imagen', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

#img = cv2.imread('ob3.jpg')
#img = imutils.resize(img, width=500) #650
#img = Detector(img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#https://thingspeak.com/channels/1597404f
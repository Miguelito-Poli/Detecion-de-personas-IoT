import os
import cv2

imagesPath = "Images"
imagesPathList = os.listdir(imagesPath)
#print('imagesPathList=', imagesPathList)

for imageName in imagesPathList:
    print('imageName=', imageName)
    image = cv2.imread(imagesPath + '/' + imageName)
    cv2.imshow('image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
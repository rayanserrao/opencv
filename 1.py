import cv2

img = cv2.imread('rayan.jpg',-1)
# print(img) - if it is none then path is wrong andn if matrix then image read is succesfull


# how to resize /rotate image
# img = cv2.resize(img,(400,400))

# half of the original one
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img = cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg',img)

# display image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()  






import cv2
import random

img = cv2.imread('rayan.jpg',1)
# print(type(img))
# print(img.shape)

# print first row
# print(img[0][45:400])

# chaning part of image
# for i in range(100):
#     for j in range(img.shape[1]):  # checking for teh columns, so[1]
#         img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]


# copy part of the image
tag = img[500:700,600:900] # numpy array
img[100:300,400:700] = tag

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 


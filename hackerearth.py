# # Program to multiply two matrices using nested loops

# 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)

#!/bin/python3

# import cv2
# import numpy as np
# kernel= np.ones((5,2),np.uint64)
# img= cv2.imread("bg.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgcany= cv2.Canny(img,100,100)
# imgdialate= cv2.dilate(imgcany,kernel, iterations=1)

# cv2.imshow("image",imgGray)
# cv2.imshow("canny",imgcany)
# cv2.imshow("canny",imgdialate)
# cv2.waitKey(0)

# cap=cv2.VideoCapture(0)
# cap.set(4,450)
# cap.set(3,650)
# cap.set(10,200)
# while True:
#     ret,frame=cap.read()
#     # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('output',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    

# print(camp([1,5,4,7]) = 10)

x,y,r=2,3,4
print(x,y,r)
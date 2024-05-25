import cv2
image=cv2.imread("images.jpeg",cv2.IMREAD_UNCHANGED)
scale_percent=50

new_width=int(image.shape[1]*scale_percent/100)
new_height=int(image.shape[0]*scale_percent/100)

output=cv2.resize(image,(new_height,new_width))

cv2.imwrite("new_image.jpeg",output)
cv2.waitKey(0)
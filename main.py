import cv2
'''image = cv2.imread("damon-elena.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("tittle", image)
cv2.waitKey(0)'''

# Configurable parameters
source = "damon-elena.jpg"
destination = 'newImage.png'
# Percent by which the image is resized
scale_percent = 50

src =cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("tittle",src)

# Calculate the 50percent of original dimension
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)

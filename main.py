import cv2

img = cv2.imread ("C:\\Users\\jayra\\Desktop\\Internship\\Documents\\E_IMG_0910.jpg", 1)

resized = cv2.resize(img, (600,600))

cv2.imshow("Jay",resized)
cv2.waitKey(2000)

cv2.destroyAllWindows()


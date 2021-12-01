def cropped_image(img):
    car=cv2.CascadeClassifier("indian_license_plate.xml")
	photo=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	plate=car.detectMultiScale(photo)
	for (x,y,w,h) in plate:
		image=photo[y:y+h,x:x+w]
		cv2.rectangle(photo,(x,y),(x+w,y+h),(0,255,0),2)
        
	return image


def fix_dimension(img): 
    new_img = np.zeros((28,28,3))
    for i in range(3):
        new_img[:,:,i] = img
    return new_img


def processed_image(image):
    img=cv2.resize(image,(300,75))
    _,binary_img=cv2.threshold(img,160,255,cv2.THRESH_BINARY)
    erode_img=cv2.erode(binary_img,(3,3))
    img_dilate = cv2.dilate(erode_img, (2,2))
    
    return img_dilate

def find_contours(img) :
    cntrs, _ = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)[:11]
    x_cntr_list = []
    target_contours = []
    img_res = []
    for cntr in cntrs :
        x, y, w, h = cv2.boundingRect(cntr)
        if ((w>=15) & (w<=340))  and h >= (processed_image.shape[0]>>1)-15:
            x_cntr_list.append(x) 
            char = img[y:y+h, x:x+w]
            char = cv2.resize(char, (20, 40))
            char = cv2.subtract(255, char)
            img_res.append(char) 
#Return characters on ascending order with respect to the x-coordinate (most-left character first)
#arbitrary function that stores sorted list of character indeces
    import numpy as np
    indices = sorted(range(len(x_cntr_list)), key=lambda k: x_cntr_list[k])
    img_res_copy = []
    for idx in indices:
        img_res_copy.append(img_res[idx])# stores character images according to their index
    img_res = np.array(img_res_copy)

    return img_res,x_cntr_list
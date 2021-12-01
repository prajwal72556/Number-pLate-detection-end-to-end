from flask import Flask,render_template,request
from keras.models import load_model
from preprocessing import *
import cv2

model=keras.models.load("Number_Plate_Production_final.h5")

app=Flask(__name__)

@app.route("/")
def index():
	#return "HEllo"
	return render_template("index1.html")




  
'''
def show_results():
    dic = {}
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i,c in enumerate(characters):
        dic[i] = c

    output = []
    for i,ch in enumerate(char): #iterating over the characters
        img_ = cv2.resize(ch, (28,28))
        img = fix_dimension(img_)
        img = img.reshape(1,28,28,3) #preparing image for the model
        predict_x=model.predict(img) 
        y=np.argmax(predict_x,axis=1)[0]
        character = dic[y] 
        output.append(character) #storing the result in a list
        
    plate_number = ''.join(output)
    
    return plate_number

'''


@app.route("/prediction",methods=["POST"])
def prediction():
	img=request.files['img']
	img.save("img.jpg")
	photo=cv2.imread("img.jpg")
	cropped_img=cropped_image(photo)
	processed_image=processed_image(cropped_img)
	char,x_list=find_contours(processed_image)
	dic = {}
    	characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    	for i,c in enumerate(characters):
        	dic[i] = c

    	output = []
    	for i,ch in enumerate(char): #iterating over the characters
        	img_ = cv2.resize(ch, (28,28))
        	img = fix_dimension(img_)
        	img = img.reshape(1,28,28,3) #preparing image for the model
        	predict_x=model.predict(img) 
        	y=np.argmax(predict_x,axis=1)[0]
        	character = dic[y] 
        	output.append(character) #storing the result in a list
        
    	data = ''.join(output)
    
    	return render_template("prediction.html",data=data)

if __name__=="__main__":
	app.run(debug=True) 
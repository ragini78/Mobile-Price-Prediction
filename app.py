# Importing the liberaries
import pickle
import numpy as np
from flask import Flask , request , render_template

#Global Variable
app = Flask(__name__)
loadModel = pickle.load(open('prediction.pkl','rb'))

#User defined functions
@app.route("/",methods = ['GET'])
def Home():
    return render_template('index.html')

@app.route('/prediction',methods = ['POST'])
def predict():
    battery_power = int(request.form['battery_power'])
    px_height = int(request.form['px_height'])
    px_width = int(request.form['px_width'])
    ram = int(request.form['ram'])

    prediction = loadModel.predict([[battery_power,px_height,px_width,ram]])
    

    if prediction == [0]:
        prediction = 'Low Cost'
    elif prediction == [1] :
        prediction = 'Medium Cost'
    elif prediction == [2] :
        prediction = 'High Cost'
    else :
        prediction = 'Very High Cost'


    return render_template('index.html',prediction_output = prediction) 

# Main Function

if __name__ == "__main__":
    app.run(debug = True)
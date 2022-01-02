import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template # For reading URL parameter 
import joblib
import pickle


# Creating flask app
app = Flask(__name__) # Initiating app

# Load pickle model
model = pickle.load(open("quadratic_discriminant_analysis.pkl", "rb"))

# Define the home page
@app.route("/",methods=['GET'])
def Home():
    return render_template("index.html")

# Predict method
@app.route("/predict",methods=["POST"])
def predict():
    if request.method == 'POST':
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        gender = int(request.form['gender'])

        bmi_predict = model.predict([[height,weight,gender]])

    return render_template("index.html", prediction_text ="Your BMI is {}".format(bmi_predict))

if __name__ == "__main__":
    app.run(debug=True)


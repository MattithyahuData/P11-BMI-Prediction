import pickle
from flask import Flask, request, jsonify, render_template # For reading URL parameter 



# Creating flask app
app = Flask(__name__) # Initiating app

# Load pickle model
model = pickle.load(open("qda_bmi_model.pkl", "rb"))

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

        BMI = round((weight / (height/100)**2),2)
        

        bmi_predict = model.predict([[height,weight]])

        if bmi_predict == 0:
            bmiclass = 'Underweight'
            return render_template("index.html", bmi_text ="BMI = {a}".format(a=BMI),  bmirange_text = "You are in the {c} range.".format(c = bmiclass), index_text = "Index {b}".format(b=bmi_predict))
        elif bmi_predict == 1:
            bmiclass = 'Normal weight'
            return render_template("index.html", bmi_text ="BMI = {a}".format(a=BMI),  bmirange_text = "You are in the {c} range.".format(c = bmiclass), index_text = "Index {b}".format(b=bmi_predict))
        elif bmi_predict == 2:
            bmiclass = 'Overweight'
            return render_template("index.html", bmi_text ="BMI = {a}".format(a=BMI),  bmirange_text = "You are in the {c} range.".format(c = bmiclass), index_text = "Index {b}".format(b=bmi_predict))
        elif bmi_predict == 3:
            bmiclass = 'Obese'
            return render_template("index.html", bmi_text ="BMI = {a}".format(a=BMI),  bmirange_text = "You are in the {c} range.".format(c = bmiclass), index_text = "Index {b}".format(b=bmi_predict))
        elif bmi_predict == 4:
            bmiclass = 'Severly Obese'
            return render_template("index.html", bmi_text ="BMI = {a}".format(a=BMI),  bmirange_text = "You are in the {c} range.".format(c = bmiclass), index_text = "Index {b}".format(b=bmi_predict))
        else:
            return 'UNKNOWN'



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)


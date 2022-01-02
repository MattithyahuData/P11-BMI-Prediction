import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
    return '<h1>API is working.. </h1>'


@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('qda_model.ml')
    predict_bmi = model.predict([[request.args['height'],
                                   request.args['weight'],
                                    request.args['gender']]])
    return str(predict_bmi)


if __name__ == "__main__":
    app.run(debug=True)

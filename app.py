# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from markupsafe import escape
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            CRIM = float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PT = float(request.form['PT'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])

            linReg_model = 'linReg_model.pickle'
            scale_model = 'scale_model.pickle'

            linReg = pickle.load(open(linReg_model, 'rb'))  # loading the Linear Regression model from file
            scaler = pickle.load(open(scale_model, 'rb'))  # loading the standard scaler model from file
            # predictions using the loaded model file
            scaled_input = scaler.transform([[CRIM, ZN, CHAS, NOX, RM, DIS, RAD, TAX, PT, B, LSTAT]])
            prediction = linReg.predict(scaled_input)
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return f"The Predicted Price for this Property is {prediction}"
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something went wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app

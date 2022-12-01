# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from application_logging import logger
import pickle

app = Flask(__name__)  # initializing a flask app

'''
def __init__(self):
    self.file_object = open("application_logging/logfile.txt", 'a+')
    self.log_writer = logger.App_Logger()
'''
@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    file_object = open("application_logging/logfile.txt", 'a+')
    log_writer = logger.App_Logger()
    if request.method == 'POST':
        try:
            log_writer.log(file_object, "Taking User Input")

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

            log_writer.log(file_object, "Initialising Linear Regression Model")
            linReg = pickle.load(open(linReg_model, 'rb'))  # loading the Linear Regression model from file
            log_writer.log(file_object, "Initializing Scaling model")
            scaler = pickle.load(open(scale_model, 'rb'))  # loading the standard scaler model from file
            # predictions using the loaded model file

            log_writer.log(file_object, "Input Scaling")
            scaled_input = scaler.transform([[CRIM, ZN, CHAS, NOX, RM, DIS, RAD, TAX, PT, B, LSTAT]])
            log_writer.log(file_object, "Generating Prediction using Trained model")
            prediction = linReg.predict(scaled_input)
            log_writer.log(file_object, f"The Predicted Price for this Property is {prediction}")
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return f"The Predicted Price for this Property is {prediction}"
        except Exception as e:
            log_writer.log(file_object, "Error Occurred!!")
            log_writer.log(file_object, f'The Exception message is: {e}')
            print('The Exception message is: ', e)
            return 'something went wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)  # running the app

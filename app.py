# importing the necessary dependencies
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from application_logging import logger
import pickle

app = Flask(__name__)  # initializing a flask app

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

            pclass = float(request.form['pclass'])
            sex = float(request.form['sex'])
            age = float(request.form['age'])
            sibsp = float(request.form['sibsp'])
            parch = float(request.form['parch'])
            fare = float(request.form['fare'])


            tree_model = 'decision_tree_titanic.pickle'

            log_writer.log(file_object, "Initialising Decision Tree Model")
            decisionTree = pickle.load(open(tree_model, 'rb'))  # loading the Linear Regression model from file

            # predictions using the loaded model file
            log_writer.log(file_object, "Generating Prediction using Trained model")
            prediction = decisionTree.predict([[pclass,sex,age,sibsp,parch,fare]])
            log_writer.log(file_object, f"Possibility of Survival of this Passanger is {prediction}")
            print('prediction is', prediction)
            # showing the prediction results in a UI
            survival = ''
            if prediction == 0:
                survival = "This Passenger Did Not survive"
            else:
                survival = "This Passenger Survived"
            return render_template("index.html", prediction=survival)
            #return f"The Predicted Price for this Property is {prediction}"
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

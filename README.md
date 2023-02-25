# Titanic Survival Predictor

This ML web app uses a decision tree model trained on the famous Titanic dataset to predict whether a passenger would have survived the disaster or not. The model considers several variables including passenger class, sex, age, siblings/spouses aboard, parents/children aboard, and fare to make its predictions.

The decision tree model was implemented using the scikit-learn library and was optimized using the hyperparameter tuning framework Optuna. With the help of Optuna, we were able to fine-tune the model's parameters to achieve optimal performance.

Using this app, users can input the aforementioned variables for any hypothetical passenger, and the model will predict their likelihood of surviving the Titanic disaster. This app could be particularly useful for historians or Titanic enthusiasts interested in exploring the factors that influenced survival rates on the fateful voyage.

### Try it out for yourself

[Titanic Survival Predictor]()

Note: The page may take up to 30 seconds to load due to platform limitation

### Dataset Description

The Titanic dataset is a popular dataset in the field of data science and machine learning. It contains information on the passengers who were aboard the Titanic when it famously sank on its maiden voyage in 1912.

The dataset contains information on 891 passengers, including whether they survived or not, as well as several other features such as age, gender, ticket class, and more. It is commonly used to predict whether a passenger would have survived the sinking based on these features.

Variable Descriptions:

    PassengerId: A unique identifier for each passenger.
    Survived: Indicates whether the passenger survived or not (0 = No, 1 = Yes).
    Pclass: The passenger's class (1 = 1st, 2 = 2nd, 3 = 3rd).
    Name: The passenger's name.
    Sex: The passenger's gender.
    Age: The passenger's age in years.
    SibSp: The number of siblings/spouses aboard the Titanic.
    Parch: The number of parents/children aboard the Titanic.
    Ticket: The passenger's ticket number.
    Fare: The fare paid by the passenger.
    Cabin: The passenger's cabin number.
    Embarked: The port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).
### Input Variables required for the prediction
'Pclass','Sex', 'Age', 'SibSp', 'Parch', 'Fare'

**Survived** is the target variable

##### PREDICT TITANIC SURVIVAL PROJECT

"""
The RMS Titanic set sail on its maiden voyage in 1912, crossing the Atlantic from Southampton, England to New York City. The ship never completed the voyage, sinking to the bottom of the Atlantic Ocean after hitting an iceberg, bringing down 1,502 of 2,224 passengers onboard.

In this project you will create a Logistic Regression model that predicts which passengers survived the sinking of the Titanic, based on features like age and class.

The data we will be using for training our model is provided by Kaggle. Feel free to make the model better on your own and submit it to the Kaggle Titanic competition!
(https://www.kaggle.com/c/titanic)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

##### Load the passenger data
passengers = pd.read_csv('/Users/maosa/Desktop/programming/codecademy/python/ml/passengers.csv')

print(passengers.head())

print(passengers.columns)

##### Update sex column to numerical
passengers.Sex = np.where(passengers.Sex == 'female', 1, 0)

##### Fill the nan values in the age column

# print(passengers['Age'].values)

passengers.Age.fillna(passengers.Age.mean(), inplace = True)

# print(passengers['Age'].values)

##### Create a first class column
passengers['FirstClass'] = np.where(passengers.Pclass == 1, 1, 0)

##### Create a second class column
passengers['SecondClass'] = np.where(passengers.Pclass == 2, 1, 0)

print(passengers.head())

print(passengers.dtypes)

##### Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]

survival = passengers['Survived']

##### Perform train, test, split
##### train_test_split() will return, in this order, the training features (X_train), the testing features (X_test), the training labels (y_train), and the testing labels (y_test)
X_train, X_test, y_train, y_test = train_test_split(features, survival)

##### Scale the feature data so it has mean = 0 and standard deviation = 1
##### Create a StandardScaler object
scaler = StandardScaler()

##### Determine the scaling factors and apply the scaling to the feature data
scaler.fit_transform(X_train)
scaler.transform(X_test)

##### Create and train the model
model = LogisticRegression(solver = 'lbfgs')

##### Fitting the model will perform gradient descent to find the feature coefficients that minimize the log-loss for the training data
model.fit(X_train, y_train)

##### Score the model on the train data. Scoring the model on the training data will run the data through the model and make final classifications on survival for each passenger in the training set. The score returned is the percentage of correct classifications, or the accuracy.
model.score(X_train, y_train)
print('\nTraining model score: %.4f%%' % model.score(X_train, y_train))

##### Score the model on the test data
model.score(X_test, y_test)
print('\nTest model score: %.4f%%\n' % model.score(X_test, y_test))

##### Analyze the coefficients
# print(features.columns)
# print('Coefficients: %s' % str(model.coef_))
print(list(zip(features.columns, model.coef_[0])))

##### Sample passenger features
##### The arrays store 4 feature values, in the following order: Sex, represented by a 0 for male and 1 for female; Age, represented as an integer in years; FirstClass, with a 1 indicating the passenger is in first class; SecondClass, with a 1 indicating the passenger is in second class

Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,24.0,1.0,0.0])

##### Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

##### Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

##### View scaled features for the sample passengers
print(sample_passengers)

##### Make survival predictions!
model.predict(sample_passengers)
print('\nSurvival predictions: %s' % str(model.predict(sample_passengers)))

##### The 1st column is the probability of a passenger perishing on the Titanic, and the 2nd column is the probability of a passenger surviving the sinking (which was calculated by our model to make the final classification decision)
model.predict_proba(sample_passengers)
print('\nSurvival probabilities: %s\n' % str(model.predict_proba(sample_passengers)))

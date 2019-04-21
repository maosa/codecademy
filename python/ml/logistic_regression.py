##### LOGISTIC REGRESSION

"""
>>>>> Introduction

When an email lands in your inbox, how does your email service know whether it’s a real email or spam? This evaluation is made billions of times per day, and one way it can be done is with Logistic Regression. Logistic Regression is a supervised machine learning algorithm that uses regression to predict the continuous probability, ranging from 0 to 1, of a data sample belonging to a specific category, or class. Then, based on that probability, the sample is classified as belonging to the more probable class, ultimately making Logistic Regression a classification algorithm.

In our spam filtering example, a Logistic Regression model would predict the probability of an incoming email being spam. If that predicted probability is greater than or equal to 0.5, the email is classified as spam. We would call spam the positive class, with the label 1, since the positive class is the class our model is looking to detect. If the predicted probability is less than 0.5, the email is classified as ham (a real email). We would call ham the negative class, with the label 0. This act of deciding which of two classes a data sample belongs to is called binary classification.

Some other examples of what we can classify with Logistic Regression include:

- Disease survival: Will a patient, 5 years after treatment for a disease, still be alive?
- Customer conversion: Will a customer arriving on a sign-up page enroll in a service?

In this lesson you will learn how to perform Logistic Regression and use it to make classifications on your own data!

>>>>> To predict the probability of a data sample belonging to a class, we:

1) initialize all feature coefficients and intercept to 0
2) multiply each of the feature coefficients by their respective feature value to get what is known as the log-odds
3) place the log-odds into the sigmoid function to link the output to the range [0,1], giving us a probability

By comparing the predicted probabilities to the actual classes of our data points, we can evaluate how well our model makes predictions and use gradient descent to update the coefficients and find the best ones for our model.

To then make a final classification, we use a classification threshold to determine whether the data sample belongs to the positive class or the negative class.

>>>>> Log-Odds

In Linear Regression we multiply the coefficients of our features by their respective feature values and add the intercept, resulting in our prediction, which can range from -∞ to +∞. In Logistic Regression, we make the same multiplication of feature coefficients and feature values and add the intercept, but instead of the prediction, we get what is called the log-odds.

The log-odds are another way of expressing the probability of a sample belonging to the positive class, or a student passing the exam. In probability, we calculate the odds of an event occurring as follows:

odds = P(event occurring) / P(event not occurring)

The odds tell us how many more times likely an event is to occur than not occur. If a student will pass the exam with probability 0.7, they will fail with probability 1 - 0.7 = 0.3. We can then calculate the odds of passing as:

odds = 0.7/0.3 = 2.33

The log-odds are then understood as the logarithm of the odds:

Log odds of passing = log(2.33) = 0.847

For our Logistic Regression model, however, we calculate the log-odds, represented by z below, by summing the product of each feature value by its respective coefficient and adding the intercept. This allows us to map our feature values to a measure of how likely it is that a data sample belongs to the positive class.

z = b0 + b1x1 + b2x2 + ... + bnxn

- b_0 is the intercept
- b_1, b_2, … b_n are the coefficients of the features x_1, x_2, … x_n

>>>>> This kind of multiplication and summing is known as a dot product.

We can perform a dot product using numpy‘s np.dot() method! Given feature matrix features, coefficient vector coefficients, and an intercept, we can calculate the log-odds in numpy as follows:

log_odds = np.dot(features, coefficients) + intercept

np.dot() will take each row, or student, in features and multiply each individual feature value by its respective coefficient in coefficients, summing the result. We then add in the intercept to get the log-odds!

How did our Logistic Regression model create the S-shaped curve we previously saw? The answer is the Sigmoid Function.

The Sigmoid Function is a special case of the more general Logistic Function, where Logistic Regression gets its name. Why is the Sigmoid Function so important? By plugging the log-odds into the Sigmoid Function, defined below, we map the log-odds z to the range [0,1].

h(z) = 1 / (1 + e^-z)

e^(-z) is the exponential function, which can be written in numpy as np.exp(-z)

This enables our Logistic Regression model to output the probability of a sample belonging to the positive class, or in our case, a student passing the final exam!

>>>>> Log-Loss I

Now that we understand how a Logistic Regression model makes its probability predictions, what coefficients and intercept should we use in our model to best predict whether a student will pass the exam? To answer this question we need a way to evaluate how well a given model fits the data we have.

The function used to evaluate the performance of a machine learning model is called a loss function, or a cost function. To evaluate how “good a fit” a model is, we calculate the loss for each data sample (how wrong the model’s prediction was) and then average the loss across all samples. The loss function for Logistic Regression, known as Log Loss.

The goal of our Logistic Regression model is to find the feature coefficients and intercept, which shape the logistic function, that minimize log-loss for our training data!

Confident correct predictions result in small losses, while confident incorrect predictions result in large losses that approach infinity. This makes sense! We want to punish our model with an increasing loss as it makes progressively incorrect predictions, and we want to reward the model with a small loss as it makes correct predictions.

Just like in Linear Regression, we can then use gradient descent to find the coefficients that minimize log-loss across all of our training data.

>>>>> Classification Thresholding

Many machine learning algorithms, including Logistic Regression, spit out a classification probability as their result. Once we have this probability, we need to make a decision on what class the sample belongs to. This is where the classification threshold comes in!

The default threshold for many algorithms is 0.5. If the predicted probability of an observation belonging to the positive class is greater than or equal to the threshold, 0.5, the classification of the sample is the positive class. If the predicted probability of an observation belonging to the positive class is less than the threshold, 0.5, the classification of the sample is the negative class.

We can choose to change the threshold of classification based on the use-case of our model. For example, if we are creating a Logistic Regression model that classifies whether or not an individual has cancer, we want to be more sensitive to the positive cases, signifying the presence of cancer, than the negative cases.

In order to ensure that most patients with cancer are identified, we can move the classification threshold down to 0.3 or 0.4, increasing the sensitivity of our model to predicting a positive cancer classification. While this might result in more overall misclassifications, we are now missing fewer of the cases we are trying to detect: actual cancer patients.

>>>>> Scikit-Learn

Now that you know the inner workings of how Logistic Regression works, let’s learn how to easily and quickly create Logistic Regression models with sklearn! sklearn is a Python library that helps build, train, and evaluate Machine Learning models.

To take advantage of sklearn‘s abilities, we can begin by creating a LogisticRegression object.

model = LogisticRegression()

After creating the object, we need to fit our model on the data. When we fit the model with sklearn it will perform gradient descent, repeatedly updating the coefficients of our model in order to minimize the log-loss. We train — or fit — the model using the .fit() method, which takes two parameters. The first is a matrix of features, and the second is a matrix of class labels.

model.fit(features, labels)

Now that the model is trained, we can access a few useful attributes of the LogisticRegression object.

- model.coef_ is a vector of the coefficients of each feature
- model.intercept_ is the intercept b_0

With our trained model we are able to predict whether new data points belong to the positive class using the .predict() method! .predict() takes a matrix of features as a parameter and returns a vector of labels 1 or 0 for each sample. In making its predictions, sklearn uses a classification threshold of 0.5.

model.predict(features)

If we are more interested in the predicted probability of the data samples belonging to the positive class than the actual class, we can use the .predict_proba() method. predict_proba() also takes a matrix of features as a parameter and returns a vector of probabilities, ranging from 0 to 1, for each sample.

model.predict_proba(features)

Before proceeding, one important note is that sklearn‘s Logistic Regression implementation requires feature data to be normalized. Normalization scales all feature data to vary over the same range. sklearn‘s Logistic Regression requires normalized feature data due to a technique called Regularization that it uses under the hood. Regularization is out of the scope of this lesson, but in order to ensure the best results from our model, we will be using a normalized version of the data from our Codecademy University example.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from exam import hours_studied_scaled, passed_exam, exam_features_scaled_train, exam_features_scaled_test, passed_exam_2_train, passed_exam_2_test, guessed_hours_scaled

##### Create and fit logistic regression model here
model = LogisticRegression()

##### Save the model coefficients and intercept here
model.fit(hours_studied_scaled, passed_exam)
calculated_coefficients = model.coef_
intercept = model.intercept_
print(calculated_coefficients)
print(intercept)

##### Predict the probabilities of passing for next semester's students here
passed_predictions = model.predict_proba(guessed_hours_scaled)

##### Create a new model on the training data with two features here
model_2 = model.fit(exam_features_scaled_train, passed_exam_2_train)

##### Predict whether the students will pass here
passed_predictions_2 = model_2.predict(exam_features_scaled_test)
print(passed_predictions_2)

"""
>>>>> Feature Importance
One of the defining features of Logistic Regression is the interpretability we have from the feature coefficients. How to handle interpreting the coefficients depends on the kind of data you are working with (normalized or not) and the specific implementation of Logistic Regression you are using. We’ll discuss how to interpret the feature coefficients from a model created in sklearn with normalized feature data.

Since our data is normalized, all features vary over the same range. Given this understanding, we can compare the feature coefficients’ magnitudes and signs to determine which features have the greatest impact on class prediction, and if that impact is positive or negative.

- Features with larger, positive coefficients will increase the probability of a data sample belonging to the positive class
- Features with larger, negative coefficients will decrease the probability of a data sample belonging to the positive class
- Features with small, positive or negative coefficients have minimal impact on the probability of a data sample belonging to the positive class

Given cancer data, a logistic regression model can let us know what features are most important for predicting survival after, for example, five years from diagnosis. Knowing these features can lead to a better understanding of outcomes, and even lives saved!
"""

##### Assign and update coefficients
coefficients = model_2.coef_
##### To visualise the coefficients
coefficients = coefficients.tolist()[0]

##### Create a bar graph comparing the feature coefficients with matplotlib‘s plt.bar() method
plt.bar([1,2],coefficients)
plt.xticks([1,2],['hours studied','math courses taken'])
plt.xlabel('feature')
plt.ylabel('coefficient')
plt.show()

"""
>>>>> Review
Congratulations! You just learned how a Logistic Regression model works and how to fit one to a dataset. Class is over, and the final exam for Codecademy University’s Introductory Machine Learning is around the corner. Do you predict that you will pass? Let’s do some review to make sure.

- Logistic Regression is used to perform binary classification, predicting whether a data sample belongs to a positive (present) class, labeled 1 and the negative (absent) class, labeled 0.

- The Sigmoid Function bounds the product of feature values and their coefficients, known as the log-odds, to the range [0,1], providing the probability of a sample belonging to the positive class.

- A loss function measures how well a machine learning model makes predictions. The loss function of Logistic Regression is log-loss.

- A Classification Threshold is used to determine the probabilistic cutoff for where a data sample is classified as belonging to a positive or negative class. The standard cutoff for Logistic Regression is 0.5, but the threshold can be higher or lower depending on the nature of the data and the situation.

- Scikit-learn has a Logistic Regression implementation that allows you to fit a model to your data, find the feature coefficients, and make predictions on new data samples.

- The coefficients determined by a Logistic Regression model can be used to interpret the relative importance of each feature in predicting the class of a data sample.
"""

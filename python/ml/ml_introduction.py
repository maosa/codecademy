"""
Machine learning can be branched out into the following categories:

Supervised Learning
Unsupervised Learning

>>>>>
Supervised Learning is where the data is labeled and the program learns to predict the output from the input data. For instance, a supervised learning algorithm for credit card fraud detection would take as input a set of recorded transactions. For each transaction, the program would predict if it is fraudulent or not.

Supervised learning problems can be further grouped into regression and classification problems.

Regression:

In regression problems, we are trying to predict a continuous-valued output. Examples are:

What is the housing price in Neo York?
What is the value of cryptocurrencies?
Classification:

In classification problems, we are trying to predict a discrete number of values. Examples are:

Is this a picture of a human or a picture of an AI?
Is this email spam?

>>>>>
Unsupervised Learning is a type of machine learning where the program learns the inherent structure of the data based on unlabeled examples.

Clustering is a common unsupervised machine learning approach that finds patterns and structures in unlabeled data by grouping them into clusters.

Some examples:

Social networks clustering topics in their news feed
Consumer sites clustering users for recommendations
Search engines to group similar objects in one cluster
"""

#####

"""
Scikit-Learn Cheatsheet

Open-source ML library for Python. Built on NumPy, SciPy, and Matplotlib.

scikit-learn

Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms. It’s built upon some of the technology you might already be familiar with, like NumPy, pandas, and Matplotlib!

As you build robust Machine Learning programs, it’s helpful to have all the sklearn commands all in one place in case you forget.

>>>>> Linear Regression

Import and create the model:

from sklearn.linear_model import LinearRegression

your_model = LinearRegression()

Fit:

your_model.fit(x_training_data, y_training_data)
.coef_: contains the coefficients
.intercept_: contains the intercept

Predict:

predictions = your_model.predict(your_x_data)
.score(): returns the coefficient of determination R²

>>>>> Naive Bayes
Import and create the model:

from sklearn.naive_bayes import MultinomialNB

your_model = MultinomialNB()

Fit:

your_model.fit(x_training_data, y_training_data)

Predict:

# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)

# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)

>>>>> K-Nearest Neighbors

Import and create the model:

from sklearn.neigbors import KNeighborsClassifier

your_model = KNeighborsClassifier()

Fit:

your_model.fit(x_training_data, y_training_data)

Predict:

# Returns a list of predicted classes - one prediction for every data point
predictions = your_model.predict(your_x_data)

# For every data point, returns a list of probabilities of each class
probabilities = your_model.predict_proba(your_x_data)

>>>>> K-Means

Import and create the model:

from sklearn.cluster import KMeans

your_model = KMeans(n_clusters=4, init='random')
n_clusters: number of clusters to form and number of centroids to generate
init: method for initialization
k-means++: K-Means++ [default]
random: K-Means
random_state: the seed used by the random number generator [optional]

Fit:

your_model.fit(x_training_data)

Predict:

predictions = your_model.predict(your_x_data)

>>>>> Validating the Model

Import and print accuracy, recall, precision, and F1 score:

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))

Import and print the confusion matrix:

from sklearn.metrics import confusion_matrix

print(confusion_matrix(true_labels, guesses))

>>>>> Training Sets and Test Sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

- train_size: the proportion of the dataset to include in the train split
- test_size: the proportion of the dataset to include in the test split
- random_state: the seed used by the random number generator [optional]
"""

##### LINEAR REGRESSION

import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 11
#intercept:
b = 45

y = [(x*m)+b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)
plt.show()

#####

x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0
y_predicted1 = [1, 2, 3]

#y = 0.5x + 1
m2 = 0.5
b2 = 1
y_predicted2 = [1.5, 2, 2.5]

total_loss1 = 0
for i, n in zip(y, y_predicted1):
  total_loss1 += (i - n)**2

total_loss2 = 0
for i, n in zip(y, y_predicted2):
  total_loss2 += (i - n)**2

print('Total loss 1: ' + str(total_loss1))
print('Total loss 2: ' + str(total_loss2))

##### GRADIENT DESCEND

def get_gradient_at_b(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -(2/N) * diff
    return b_gradient


def get_gradient_at_m(x, y, b, m):
    N = len(x)
    diff = 0
    for i in range(N):
        x_val = x[i]
        y_val = y[i]
        diff += x_val * (y_val - ((m * x_val) + b))
    m_gradient = -(2/N) * diff
    return m_gradient


##### Define your step_gradient function here
##### The learning rate in this case is 0.01
def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)
    return [b, m]


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

##### current intercept guess:
b = 0
##### current slope guess:
m = 0

##### Call your function here to update b and m
b, m = step_gradient(months, revenue, b, m)
print(b, m)

#####

##### Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

##### Your gradient_descent function here:
def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)
    return [b, m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

b, m = gradient_descent(months, revenue, 0.01, 1000)

y = [m*x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)
plt.show()

#####

"""
Scikit-learn, or sklearn, is used specifically for Machine Learning. Inside the linear_model module, there is a LinearRegression() function we can use:

from sklearn.linear_model import LinearRegression

You can first create a LinearRegression model, and then fit it to your x and y data:

line_fitter = LinearRegression()
line_fitter.fit(X, y)

The .fit() method gives the model two variables that are useful to us:

1) the line_fitter.coef_, which contains the slope
2) the line_fitter.intercept_, which contains the intercept

We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:

y_predicted = line_fitter.predict(X)

Note: the num_iterations and the learning_rate that you learned about in your own implementation have default values within scikit-learn, so you don’t need to worry about setting them specifically!
"""

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
line_fitter.fit(temperature, sales)
sales_predict = line_fitter.predict(temperature)

plt.plot(temperature, sales, 'o')
plt.plot(temperature, sales_predict)
plt.show()

#####

"""
Review
We have seen how to implement a linear regression algorithm in Python, and how to use the linear regression model from scikit-learn. We learned:

- We can measure how well a line fits by measuring loss.
- The goal of linear regression is to minimize loss.
- To find the line of best fit, we try to find the b value (intercept) and the m value (slope) that minimize loss.
- Convergence refers to when the parameters stop changing with each iteration.
- Learning rate refers to how much the parameters are changed on each iteration.

We can use Scikit-learn’s LinearRegression() model to perform linear regression on a set of points.
"""

#####

"""
Euclidean Distance is the most commonly used distance formula. To find the Euclidean distance between two points, we first calculate the squared distance between each dimension. If we add up all of these squared differences and take the square root, we’ve computed the Euclidean distance.
"""

def euclidean_distance(pt1, pt2):
    distance = 0
    for p1, p2 in zip(pt1, pt2):
        distance += (p1 - p2)**2
    return distance**0.5

print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))

"""
Manhattan Distance is extremely similar to Euclidean distance. Rather than summing the squared difference between each dimension, we instead sum the absolute value of the difference between each dimension. It’s called Manhattan distance because it’s similar to how you might navigate when walking city blocks. If you’ve ever wondered “how many blocks will it take me to get from point A to point B”, you’ve computed the Manhattan distance. Note that Manhattan distance will always be greater than or equal to Euclidean distance.
"""

def manhattan_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance

print(manhattan_distance([1, 2], [4, 0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))

"""
Hamming Distance is another slightly different variation on the distance formula. Instead of finding the difference of each dimension, Hamming distance only cares about whether the dimensions are exactly equal. When finding the Hamming distance between two points, add one for every dimension that has different values. Hamming distance is used in spell checking algorithms. For example, the Hamming distance between the word “there” and the typo “thete” is one. Each letter is a dimension, and each dimension has the same value except for one.
"""

def hamming_distance(pt1, pt2):
    distance = 0
    for p1, p2 in zip(pt1, pt2):
        if p1 != p2:
            distance += 1
        else:
            pass
    return distance

print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))

"""
Now that you’ve written these three distance formulas yourself, let’s look at how to use them using Python’s SciPy library:

- Euclidean Distance .euclidean()
- Manhattan Distance .cityblock()
- Hamming Distance .hamming()

There are a few noteworthy details to talk about:

First, the scipy implementation of Manhattan distance is called cityblock(). Remember, computing Manhattan distance is like asking how many blocks away you are from a point.

Second, the scipy implementation of Hamming distance will always return a number between 0 an 1. Rather than summing the number of differences in dimensions, this implementation sums those differences and then divides by the total number of dimensions. For example, in your implementation, the Hamming distance between [1, 2, 3] and [7, 2, -10] would be 2. In scipy‘s version, it would be 2/3.
"""

from scipy.spatial import distance

print('\nUser defined distance functions:')
print(euclidean_distance([1, 2], [4, 0]))
print(manhattan_distance([1, 2], [4, 0]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))

print('\nSciPy distance functions:')
print(distance.euclidean([1, 2], [4, 0]))
print(distance.cityblock([1, 2], [4, 0]))
print(distance.hamming([5, 4, 9], [1, 7, 9]))

##### NORMALIZATION

"""
Many machine learning algorithms attempt to find trends in the data by comparing features of data points. However, there is an issue when the features are on drastically different scales.

For example, consider a dataset of houses. Two potential features might be the number of rooms in the house, and the total age of the house in years. A machine learning algorithm could try to predict which house would be best for you. However, when the algorithm compares data points, the feature with the larger scale will completely dominate the other.

When the data looks squished like that, we know we have a problem. The machine learning algorithm should realize that there is a huge difference between a house with 2 rooms and a house with 20 rooms. But right now, because two houses can be 100 years apart, the difference in the number of rooms contributes less to the overall difference.

As a more extreme example, imagine what the graph would look like if the x-axis was the cost of the house. The data would look even more squished; the difference in the number of rooms would be even less relevant because the cost of two houses could have a difference of thousands of dollars.

The goal of normalization is to make every datapoint have the same scale so each feature is equally important.

>>>>> Min-Max Normalization

Min-max normalization is one of the most common ways to normalize data. For every feature, the minimum value of that feature gets transformed into a 0, the maximum value gets transformed into a 1, and every other value gets transformed into a decimal between 0 and 1.

For example, if the minimum value of a feature was 20, and the maximum value was 40, then 30 would be transformed to about 0.5 since it is halfway between 20 and 40. The formula is as follows:

value - min / max - min

Min-max normalization has one fairly significant downside: it does not handle outliers very well. For example, if you have 99 values between 0 and 40, and one value is 100, then the 99 values will all be transformed to a value between 0 and 0.4. That data is just as squished as before!

Normalizing fixed the squishing problem on the y-axis, but the x-axis is still problematic. Now if we were to compare these points, the y-axis would dominate; the y-axis can differ by 1, but the x-axis can only differ by 0.4.

>>>>> Z-Score Normalization

Z-score normalization is a strategy of normalizing data that avoids this outlier issue. The formula for Z-score normalization is below:

value - μ / σ

Here, μ is the mean value of the feature and σ is the standard deviation of the feature. If a value is exactly equal to the mean of all the values of the feature, it will be normalized to 0. If it is below the mean, it will be a negative number, and if it is above the mean it will be a positive number. The size of those negative and positive numbers is determined by the standard deviation of the original feature. If the unnormalized data had a large standard deviation, the normalized values will be closer to 0.

Take a look at the graph below. This is the same data as before, but this time we’re using z-score normalization.

While the data still looks squished, notice that the points are now on roughly the same scale for both features — almost all points are between -2 and 2 on both the x-axis and y-axis. The only potential downside is that the features aren’t on the exact same scale.

With min-max normalization, we were guaranteed to reshape both of our features to be between 0 and 1. Using z-score normalization, the x-axis now has a range from about -1.5 to 1.5 while the y-axis has a range from about -2 to 2. This is certainly better than before; the x-axis, which previously had a range of 0 to 40, is no longer dominating the y-axis.

>>>>> Review
Normalizing your data is an essential part of machine learning. You might have an amazing dataset with many great features, but if you forget to normalize, one of those features might completely dominate the others. It’s like you’re throwing away almost all of your information! Normalizing solves this problem. In this article, you learned the following techniques to normalize:

1) Min-max normalization: Guarantees all features will have the exact same scale but does not handle outliers well.
2) Z-score normalization: Handles outliers, but does not produce normalized data with the exact same scale.
"""

##### TRAINING SET VS VALIDATION SET

"""
>>>>> Testing Our Model
Supervised machine learning algorithms are amazing tools capable of making predictions and classifications. However, it is important to ask yourself how accurate those predictions are. After all, it’s possible that every prediction your classifier makes is actually wrong! Luckily, we can leverage the fact that supervised machine learning algorithms, by definition, have a dataset of pre-labeled datapoints. In order to test the effectiveness of your algorithm, we’ll split this data into:

- training set
- validation set
- test set

>>>>> Training Set vs Validation Set
The training set is the data that the algorithm will learn from. Learning looks different depending on which algorithm you are using. For example, when using Linear Regression, the points in the training set are used to draw the line of best fit. In K-Nearest Neighbors, the points in the training set are the points that could be the neighbors.

After training using the training set, the points in the validation set are used to compute the accuracy or error of the classifier. The key insight here is that we know the true labels of every point in the validation set, but we’re temporarily going to pretend like we don’t. We can use every point in the validation set as input to our classifier. We’ll then receive a classification for that point. We can now peek at the true label of the validation point and see whether we got it right or not. If we do this for every point in the validation set, we can compute the validation error!

Validation error might not be the only metric we’re interested in. A better way of judging the effectiveness of a machine learning algorithm is to compute its precision, recall, and F1 score.

>>>>> How to Split
Figuring out how much of your data should be split into your validation set is a tricky question. If your training set is too small, then your algorithm might not have enough data to effectively learn. On the other hand, if your validation set is too small, then your accuracy, precision, recall, and F1 score could have a large variance. You might happen to get a really lucky or a really unlucky split! In general, putting 80% of your data in the training set, and 20% of your data in the validation set is a good place to start.

>>>>> N-Fold Cross-Validation
Sometimes your dataset is so small, that splitting it 80/20 will still result in a large amount of variance. One solution to this is to perform N-Fold Cross-Validation. The central idea here is that we’re going to do this entire process N times and average the accuracy. For example, in 10-fold cross-validation, we’ll make the validation set the first 10% of the data and calculate accuracy, precision, recall and F1 score. We’ll then make the validation set the second 10% of the data and calculate these statistics again. We can do this process 10 times, and every time the validation set will be a different chunk of the data. If we then average all of the accuracies, we will have a better sense of how our model does on average.

>>>>> Changing The Model / Test Set
Understanding the accuracy of your model is invaluable because you can begin to tune the parameters of your model to increase its performance. For example, in the K-Nearest Neighbors algorithm, you can watch what happens to accuracy as you increase or decrease K. You can also use this information to try to avoid overfitting or underfitting your data. (You can try out all of this in our K-Nearest Neighbors lesson!)

Once you’re happy with your model’s performance, it is time to introduce the test set. This is part of your data that you partitioned away at the very start of your experiment. It’s meant to be a substitute for the data in the real world that you’re actually interested in classifying. It functions very similarly to the validation set, except you never touched this data while building or tuning your model. By finding the accuracy, precision, recall, and F1 score on the test set, you get a good understanding of how well your algorithm will do in the real world.
"""

##### Accuracy, precision, recall, and F1 score

"""
>>>>> Accuracy

After creating a machine learning algorithm capable of making classifications, the next step in the process is to calculate its predictive power. In order to calculate these statistics, we’ll need to split our data into a training set and validation set.

Let’s say you’re using a machine learning algorithm to try to predict whether or not you will get above a B on a test. The features of your data could be something like:

The number of hours you studied this week.
The number of hours you watched Netflix this week.
The time you went to bed the night before the test.
Your average in the class before taking the test.
The simplest way of reporting the effectiveness of an algorithm is by calculating its accuracy. Accuracy is calculated by finding the total number of correctly classified points and dividing by the total number of points.

In other words, accuracy can be defined as:

True positives+True negatives / True positives+True negatives+False positives+False negatives

Let’s define those terms in the context of our grade example :

True Positive: The algorithm predicted you would get above a B, and you did.
True Negative: The algorithm predicted you would get below a B, and you did.
False Positive: The algorithm predicted you would get above a B, and you didn’t.
False Negative: The algorithm predicted you would get below a B, and you didn’t.
"""

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0

for l, g in zip(labels, guesses):
    if (l == 1) & (g == 1):
        true_positives += 1
    elif (l == 0) & (g == 0):
        true_negatives += 1
    elif (l == 0) & (g == 1):
        false_positives += 1
    elif (l == 1) & (g == 0):
        false_negatives += 1

accuracy = (true_positives + true_negatives)/(true_positives + true_negatives + false_positives + false_negatives)

print(accuracy)

"""
>>>>> Recall

Accuracy can be an extremely misleading statistic depending on your data. Consider the example of an algorithm that is trying to predict whether or not there will be over 3 feet of snow on the ground tomorrow. We can write a pretty accurate classifier right now: always predict False. This classifier will be incredibly accurate — there are hardly ever many days with that much snow. But this classifier never finds the information we’re actually interested in.

In this situation, the statistic that would be helpful is recall. Recall measures the percentage of relevant items that your classifier found. In this example, recall is the number of snow days the algorithm correctly predicted divided by the total number of snow days. Another way of saying this is:

True positives / True positives + False negatives

Our algorithm that always predicts False might have a very high accuracy, but it never will find any True Positives, so its recall is 0. This makes sense; recall should be very low for such an absurd classifier.
"""

recall = true_positives / (true_positives + false_negatives)
print(recall)

"""
>>> Precision

Unfortunately, recall isn’t a perfect statistic either. For example, we could create a snow day classifier that always returns True. This would have low accuracy, but its recall would be 1 because it would be able to accurately find every snow day. But this classifier is just as nonsensical as the one before! The statistic that will help demonstrate that this algorithm is flawed is precision.

In the snow day example, precision is the number of snow days the algorithm correctly predicted divided by the number of times it predicted there would be a snow day. The formula for precision is below:

True positives / True positives + False positives

The algorithm that predicts every day is a snow day has recall of 1, but it will have very low precision. It correctly predicts every snow day, but there are tons of false positives as well.

Precision and recall are statistics that are on opposite ends of a scale. If one goes down, the other will go up.
"""

precision = true_positives / (true_positives + false_positives)
print(precision)

"""
>>>>> F1 score

It is useful to consider the precision and recall of an algorithm, however, we still don’t have one number that can sufficiently describe how effective our algorithm is. This is the job of the F1 score — F1 score is the harmonic mean of precision and recall. The harmonic mean of a group of numbers is a way to average them together. The formula for F1 score is below:

(2 * precision * recall) / (precision + recall)

The F1 score combines both precision and recall into a single statistic. We use the harmonic mean rather than the traditional arithmetic mean because we want the F1 score to have a low value when either precision or recall is 0.

For example, consider a classifier where recall = 1 and precision = 0.01. We know that there is most likely a problem with this classifier since the precision is so low, and so we want the F1 score to reflect that.

If we took the arithmetic mean, we’d get: 1 + 0.01 / 2 = 0.505

That looks way too high! But if we calculate the harmonic mean, we get:
(2 * 1 * 0.01) / (1 + 0.01) = 0.019

That’s much better! The F1 score is now accurately describing the effectiveness of this classifier.
"""

f_1 = (2 * precision * recall) / (precision + recall)
print(f_1)

"""
>>>>> Review
You’ve now learned many different ways to analyze the predictive power of your algorithm. Some of the key insights for this course include:

- Classifying a single point can result in a true positive (truth = 1, guess = 1), a true negative (truth = 0, guess = 0), a false positive (truth = 0, guess = 1), or a false negative (truth = 1, guess = 0).
- Accuracy measures how many classifications your algorithm got correct out of every classification it made.
- Recall measures the percentage of the relevant items your classifier was able to successfully find.
- Precision measures the percentage of items your classifier found that were actually relevant.
- Precision and recall are tied to each other. As one goes up, the other will go down.
- F1 score is a combination of precision and recall.
- F1 score will be low if either precision or recall is low.

The decision to use precision, recall, or F1 score ultimately comes down to the context of your classification. Maybe you don’t care if your classifier has a lot of false positives. If that’s the case, precision doesn’t matter as much.

As long as you have an understanding of what question you’re trying to answer, you should be able to determine which statistic is most relevant to you.

The Python library scikit-learn has some functions that will calculate these statistics for you!
"""

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

labels = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
guesses = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

print(accuracy_score(labels, guesses))
print(recall_score(labels, guesses))
print(precision_score(labels, guesses))
print(f1_score(labels, guesses))

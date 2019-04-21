##### K-NEAREST NEIGHBORS CLASSIFIER

"""
K-Nearest Neighbors (KNN) is a classification algorithm. The central idea is that data points with similar attributes tend to fall into similar categories.

Consider the image to the right. This image is complicated, but for now, let’s just focus on where the data points are being placed. Every data point — whether its color is red, green, or white — has an x value and a y value. As a result, it can be plotted on this two-dimensional graph.

Next, let’s consider the color of the data. The color represents the class that the K-Nearest Neighbor algorithm is trying to classify. In this image, data points can either have the class green or the class red. If a data point is white, this means that it doesn’t have a class yet. The purpose of the algorithm is to classify these unknown points.

Finally, consider the expanding circle around the white point. This circle is finding the k nearest neighbors to the white point. When k = 3, the circle is fairly small. Two of the three nearest neighbors are green, and one is red. So in this case, the algorithm would classify the white point as green. However, when we increase k to 5, the circle expands, and the classification changes. Three of the nearest neighbors are red and two are green, so now the white point will be classified as red.

This is the central idea behind the K-Nearest Neighbor algorithm. If you have a dataset of points where the class of each point is known, you can take a new point with an unknown class, find it’s nearest neighbors, and classify it.
"""

#####

"""
In the next three lessons, we’ll implement the three steps of the K-Nearest Neighbor Algorithm:

1) Normalize the data
2) Find the k nearest neighbors
3) Classify the new point based on those neighbors
"""

def min_max_normalize(lst):
    minimum = min(lst)
    maximum = max(lst)
    max_min_diff = maximum - minimum
    normalized = []
    for i in lst:
        normalized.append((i - minimum)/(max_min_diff))
    return normalized

#####

##### COMMENTED OUT AS THIS WILL GENERATE AN ERROR
# from movies import training_set, training_labels, validation_set, validation_labels

def distance(movie1, movie2):
    squared_difference = 0
    for i in range(len(movie1)):
        squared_difference += (movie1[i] - movie2[i]) ** 2
    final_distance = squared_difference ** 0.5
    return final_distance

def classify(unknown, dataset, labels, k):
    distances = []
    #Looping through all points in the dataset
    for title in dataset:
        movie = dataset[title]
        distance_to_point = distance(movie, unknown)
        #Adding the distance and point associated with that distance
        distances.append([distance_to_point, title])
    distances.sort()
    #Taking only the k closest points
    neighbors = distances[0:k]
    num_good = 0
    num_bad = 0
    for neighbor in neighbors:
        title = neighbor[1]
        if labels[title] == 0:
            num_bad += 1
        elif labels[title] == 1:
            num_good += 1
    if num_good > num_bad:
        return 1
    else:
        return 0

"""
You’ve now built your first K Nearest Neighbors algorithm capable of classification. You can feed your program a never-before-seen movie and it can predict whether its IMDb rating was above or below 7.0. However, we’re not done yet. We now need to report how effective our algorithm is. After all, it’s possible our predictions are totally wrong!

As with most machine learning algorithms, we have split our data into a training set and validation set.

Once these sets are created, we will want to use every point in the validation set as input to the K Nearest Neighbor algorithm. We will take a movie from the validation set, compare it to all the movies in the training set, find the K Nearest Neighbors, and make a prediction. After making that prediction, we can then peek at the real answer (found in the validation labels) to see if our classifier got the answer correct.

If we do this for every movie in the validation set, we can count the number of times the classifier got the answer right and the number of times it got it wrong. Using those two numbers, we can compute the validation accuracy.

Validation accuracy will change depending on what K we use. In the next exercise, we’ll use the validation accuracy to pick the best possible K for our classifier.
"""

def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
    num_correct = 0.0
    for movie in validation_set:
        guess = classify(validation_set[movie], training_set, training_labels, k)
        if guess == validation_labels[movie]:
            num_correct += 1
    return num_correct/len(validation_set)


# print(find_validation_accuracy(training_set,training_labels,validation_set,validation_labels,3))

#####

"""
>>>>> Using sklearn

You’ve now written your own K-Nearest Neighbor classifier from scratch! However, rather than writing your own classifier every time, you can use Python’s sklearn library. sklearn is a Python library specifically used for Machine Learning. It has an amazing number of features, but for now, we’re only going to investigate its K-Nearest Neighbor classifier.

There are a couple of steps we’ll need to go through in order to use the library. First, you need to create a KNeighborsClassifier object. This object takes one parameter - k. For example, the code below will create a classifier where k = 3

classifier = KNeighborsClassifier(n_neighbors = 3)

Next, we’ll need to train our classifier. The .fit() method takes two parameters. The first is a list of points, and the second is the labels associated with those points. So for our movie example, we might have something like this

training_points = [
  [0.5, 0.2, 0.1],
  [0.9, 0.7, 0.3],
  [0.4, 0.5, 0.7]
]

training_labels = [0, 1, 1]

classifier.fit(training_points, training_labels)

Finally, after training the model, we can classify new points. The .predict() method takes a list of points that you want to classify. It returns a list of its guesses for those points.

unknown_points = [
  [0.2, 0.1, 0.7],
  [0.4, 0.7, 0.6],
  [0.5, 0.8, 0.1]
]

guesses = classifier.predict(unknown_points)
"""

from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)

classifier.fit(movie_dataset, labels)

new_movies = [[.45, .2, .5], [.25, .8, .9], [.1, .1, .9]]

guesses = classifier.predict(new_movies)

print(guesses)

"""
>>>>> Review
Congratulations! You just implemented your very own classifier from scratch and used Python’s sklearn library. In this lesson, you learned some techniques very specific to the K-Nearest Neighbor algorithm, but some general machine learning techniques as well. Some of the major takeaways from this lesson include:

- Data with n features can be conceptualized as points lying in n-dimensional space.
- Data points can be compared by using the distance formula. Data points that are similar will have a smaller distance between them.
- A point with an unknown class can be classified by finding the k nearest neighbors
- To verify the effectiveness of a classifier, data with known classes can be split into a training set and a validation set. Validation error can then be calculated.
- Classifiers have parameters that can be tuned to increase their effectiveness. In the case of K-Nearest Neighbors, k can be changed.
- A classifier can be trained improperly and suffer from overfitting or underfitting. In the case of K-Nearest Neighbors, a low k often leads to overfitting and a large k often leads to underfitting.
- Python’s sklearn library can be used for many classification and machine learning algorithms.
"""

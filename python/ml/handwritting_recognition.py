##### HANDWRITING RECOGNITION - K-MEANS CLUSTERING PROJECT

"""
>>>>> Handwriting Recognition using K-Means

The U.S. Postal Service has been using machine learning and scanning technologies since 1999. Because its postal offices have to look at roughly half a billion pieces of mail every day, they have done extensive research and developed very efficient algorithms for reading and understanding addresses. And not only the post office:

- ATMs can recognize handwritten bank checks
- Evernote can recognize handwritten task lists
- Expensify can recognize handwritten receipts
"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets

digits = datasets.load_digits()
print(digits)

print(digits.DESCR)

print(digits.data)

print(digits.target)

##### To visualize the data images, we need to use Matplotlib
plt.gray()
plt.matshow(digits.images[100])
plt.show()

##### Check if the number in the image in number 4
print(digits.target[100])

from sklearn.cluster import KMeans

##### The random_state will ensure that every time you run your code, the model is built in the same way. This can be any number. We used random_state = 42
model = KMeans(n_clusters = 10, random_state = 42)

model.fit(digits.data)

fig = plt.figure(figsize = (8, 3))
fig.suptitle('Cluser Center Images', fontsize = 14, fontweight = 'bold')

##### Scikit-learn sometimes calls centroids "cluster centers". Write a for loop to displays each of the cluster_centers_
for i in range(10):
    ##### Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)
    ##### Display images
    ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap = plt.cm.binary)

##### The cluster centers should be a list with 64 values (0-16). Here, we are making each of the cluster centers into an 8x8 2D array
##### These are the centroids of handwriting from thirty different people
plt.show()

##### What year will robots take over the world? (used mouse to wrtie down the year 2457 and copied the result into new_samples)
new_samples = np.array([
[0.00,0.35,2.13,2.28,0.68,0.00,0.00,0.00,0.05,5.56,7.62,7.62,5.45,0.00,0.00,0.00,1.67,7.62,3.99,4.94,7.31,0.00,0.00,0.00,1.06,5.87,1.29,3.81,7.62,0.00,0.00,0.00,0.00,0.00,0.00,4.34,7.53,0.00,0.00,0.00,0.00,0.00,0.29,7.07,6.09,2.26,1.96,0.00,0.00,0.36,5.84,7.62,7.62,7.62,7.55,0.38,0.00,0.75,5.94,4.40,2.54,1.27,0.53,0.00],
[0.00,0.00,0.88,2.29,2.29,2.29,1.25,0.00,0.00,0.88,6.69,7.62,7.62,7.62,7.54,1.80,0.00,3.80,7.62,2.73,0.84,1.57,7.62,3.04,0.00,4.57,6.93,0.00,0.00,1.67,7.62,2.66,0.00,4.49,7.16,1.04,0.15,5.25,7.47,0.53,0.00,1.97,7.39,7.62,7.62,7.62,3.57,0.00,0.00,0.00,0.97,3.03,3.05,1.98,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.16,5.33,5.34,5.33,6.25,7.52,1.65,0.00,6.02,6.94,5.33,5.33,5.18,3.64,0.38,0.00,6.09,6.48,3.81,3.79,2.47,0.15,0.00,0.00,4.87,6.86,6.86,7.37,7.62,5.53,0.00,0.00,0.00,0.00,0.00,0.20,4.57,7.62,0.00,0.00,1.58,4.57,4.57,4.63,6.83,7.15,0.00,0.00,2.44,6.10,6.10,6.10,5.59,1.87,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,6.15,6.86,6.86,6.86,6.86,3.40,0.00,0.00,3.19,3.81,3.81,5.02,7.62,3.74,0.00,0.00,0.00,0.00,0.00,4.57,7.24,0.61,0.00,0.00,0.00,4.77,6.92,7.61,7.47,2.04,0.00,0.00,0.00,2.44,6.02,7.62,4.26,0.91,0.00,0.00,0.00,0.00,6.55,5.80,0.00,0.00,0.00,0.00,0.00,2.21,7.62,2.89,0.00,0.00,0.00]
])

new_labels = model.predict(new_samples)

##### But wait, because this is a clustering algorithm, we dont know which label is which. By looking at the cluster centers, lets map out each of the labels with the digits we think it represents
for i in range(len(new_labels)):
    if new_labels[i] == 0:
        print(0, end='')
    elif new_labels[i] == 1:
        print(9, end='')
    elif new_labels[i] == 2:
        print(2, end='')
    elif new_labels[i] == 3:
        print(1, end='')
    elif new_labels[i] == 4:
        print(6, end='')
    elif new_labels[i] == 5:
        print(8, end='')
    elif new_labels[i] == 6:
        print(4, end='')
    elif new_labels[i] == 7:
        print(5, end='')
    elif new_labels[i] == 8:
        print(7, end='')
    elif new_labels[i] == 9:
        print(3, end='')

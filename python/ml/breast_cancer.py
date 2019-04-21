##### BREAST CANCER CLASSIFIER - KNN PROJECT

from sklearn.datasets import load_breast_cancer

breast_cancer_data = load_breast_cancer()

print(breast_cancer_data.data[0])

print(breast_cancer_data.feature_names)

print(breast_cancer_data.target)

##### 0: malignant
##### 1: benign
print(breast_cancer_data.target_names)

from sklearn.model_selection import train_test_split

##### It takes several parameters: The data you want to split (for us breast_cancer_data.data). The labels associated with that data (for us, breast_cancer_data.target). The test_size. This is what percentage of your data you want to be in your testing set. Lets use test_size = 0.2 and random_state. This will ensure that every time you run your code, the data is split in the same way. This can be any number. We used random_state = 100

##### Right now were not storing the return value of train_test_split. train_test_split returns four values in the following order: The training set, the validation set, the training labels, the validation labels

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

print(len(training_data))
print(len(training_labels))
##### Should print the same value

from sklearn.neighbors import KNeighborsClassifier

accuracies = []

for k in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(training_data, training_labels)
    ##### Let's find how accurate it is on the validation set
    print('k =', k, ':', classifier.score(validation_data, validation_labels))
    accuracies.append(classifier.score(validation_data, validation_labels))

import matplotlib.pyplot as plt

k_list = range(1, 101)

plt.plot(k_list, accuracies)
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()

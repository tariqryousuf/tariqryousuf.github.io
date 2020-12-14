import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from micromlgen import port
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import ADASYN
from sklearn.neural_network import MLPClassifier

def haar_transform(x, n):
    y = []
    for i in range(0, int((n/2)-1)):
        y.append((x[2*i] + x[(2*i) + 1]) / 2)

    return y

X_raw = np.zeros((300, 384))
X = np.zeros((300, 93))


results = []
with open("clockwise_circle_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j][i%128] = results[i][0]
        X_raw[j][128 + (i%128)] = results[i][1]
        X_raw[j][256 + (i%128)] = results[i][2]



results = []
with open("counter_clockwise_circle_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 50][i%128] = results[i][0]
        X_raw[j + 50][128 + (i%128)] = results[i][1]
        X_raw[j + 50][256 + (i%128)] = results[i][2]


results = []
with open("downward_arrow_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 100][i%128] = results[i][0]
        X_raw[j + 100][128 + (i%128)] = results[i][1]
        X_raw[j + 100][256 + (i%128)] = results[i][2]




results = []
with open("left_arrow_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 150][i%128] = results[i][0]
        X_raw[j + 150][128 + (i%128)] = results[i][1]
        X_raw[j + 150][256 + (i%128)] = results[i][2]



results = []
with open("right_arrow_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 200][i%128] = results[i][0]
        X_raw[j + 200][128 + (i%128)] = results[i][1]
        X_raw[j + 200][256 + (i%128)] = results[i][2]



results = []
with open("upward_arrow_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 250][i%128] = results[i][0]
        X_raw[j + 250][128 + (i%128)] = results[i][1]
        X_raw[j + 250][256 + (i%128)] = results[i][2]



for i in range(0, 300):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


y = np.zeros(300)
y[50:100] = np.ones(50)
y[100:150] = np.full(50, 2)
y[150:200] = np.full(50, 3)
y[200:250] = np.full(50, 4)
y[250:300] = np.full(50, 5)





X_raw_noise = np.zeros((300, 384))
for i in range(0, 300):
    mean_x = np.mean(X_raw[i][0:128])
    std_x = np.std(X_raw[i][0:128])
    mean_y = np.mean(X_raw[i][128:256])
    std_y = np.std(X_raw[i][128:256])
    mean_z = np.mean(X_raw[i][256:384])
    std_z = np.std(X_raw[i][256:384])
    X_raw_noise[i][0:128] = X_raw[i][0:128] + np.random.normal(0, std_x/2, 128)
    X_raw_noise[i][128:256] = X_raw[i][128:256] + np.random.normal(0, std_y/2, 128)
    X_raw_noise[i][256:384] = X_raw[i][256:384] + np.random.normal(0, std_z/2, 128)


'''
plt.plot(range(1, 129), X_raw[0][0:128], label="X")
plt.plot(range(1, 129), X_raw[0][128:256], label="Y")
plt.plot(range(1, 129), X_raw[0][256:384], label="Z")
plt.legend()
plt.show()

plt.plot(range(1, 129), X_raw_noise[0][0:128], label="X")
plt.plot(range(1, 129), X_raw_noise[0][128:256], label="Y")
plt.plot(range(1, 129), X_raw_noise[0][256:384], label="Z")
plt.legend()
plt.show()

plt.plot(range(1, 32), X[0][0:31], label="X")
plt.plot(range(1, 32), X[0][31:62], label="Y")
plt.plot(range(1, 32), X[0][62:93], label="Z")
plt.legend()
plt.show()
'''

X_noise = np.zeros((300, 93))
for i in range(0, 300):
    x_haar_1 = haar_transform(X_raw_noise[i][0:128], 128)
    X_noise[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw_noise[i][128:256], 128)
    X_noise[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw_noise[i][256:384], 128)
    X_noise[i][62:93] = haar_transform(z_haar_1, 64)



# Create a fake larger dataset so that we can force ADASYN to duplicate outliers

# Adding more upward arrow outliers
X_large = np.concatenate((X[0:50], X[0:20], X[50:100], X[50:70], X[100:150], X[100:120], X[150:200], X[150:170], X[200:250], X[200:220], X[250:270]))
y_large = np.concatenate((y[0:50], y[0:20], y[50:100], y[50:70], y[100:150], y[100:120], y[150:200], y[150:170], y[200:250], y[200:220], y[250:270]))
oversample = ADASYN()
X_new, y_new = oversample.fit_resample(X_large, y_large)
X_5_outliers = np.array(X_new[370:390])


# Adding more left arrow outliers
X_large = np.concatenate((X[0:50], X[0:20], X[50:100], X[50:70], X[100:150], X[100:120], X[150:170], X[200:250], X[200:220], X[250:300], X[250:270]))
y_large = np.concatenate((y[0:50], y[0:20], y[50:100], y[50:70], y[100:150], y[100:120], y[150:170], y[200:250], y[200:220], y[250:300],  y[250:270]))
oversample = ADASYN()
X_new, y_new = oversample.fit_resample(X_large, y_large)
X_3_outliers = np.array(X_new[370:390])


# Creating improved upsampled training data
X_up = np.concatenate((X_noise, X_3_outliers, X_5_outliers))
y_up = np.concatenate((y, np.full(20, 3), np.full(20, 5)))



# Testing out varius classifiers

# Training SVM model with old training data (for comparison)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
clf = SVC(kernel='rbf', gamma=0.01)
clf.fit(X_train, y_train)
train_error = 1 - clf.score(X_train, y_train)
print(train_error)
test_error = 1 - clf.score(X_test, y_test)
print(test_error)



# Training SVM model with improved training data
X_train, X_test, y_train, y_test = train_test_split(X_up, y_up, test_size=0.2, random_state=5)
clf = SVC(kernel='rbf', gamma=0.01)
clf.fit(X_train, y_train)
train_error = 1 - clf.score(X_train, y_train)
print(train_error)
test_error = 1 - clf.score(X_test, y_test)
print(test_error)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
clf = MLPClassifier(solver='lbfgs')
clf.fit(X_train, y_train)
train_error = 1 - clf.score(X_train, y_train)
print(train_error)
test_error = 1 - clf.score(X_test, y_test)
print(test_error)

# Looping through sevaral training data splits to find average accuracy
Base_error = np.zeros(51)
SMOTE_error = np.zeros(51)
NN_error = np.zeros(51)
test_size = np.zeros(51)
for j in range(0, 51):
    base_test_error = 0.0
    SMOTE_test_error = 0.0
    NN_test_error = 0.0
    for i in range(1, 101):
        # Training SVM with old training data
        test_size[j] = 0.1 + (0.7*(j/50))
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1 + (0.7*(j/50)), random_state=i)
        clf = SVC(kernel='rbf', gamma=0.01)
        clf.fit(X_train, y_train)
        base_test_error += 1 - clf.score(X_test, y_test)

        # Training SVM model with improved training data
        X_train, X_test, y_train, y_test = train_test_split(X_up, y_up, test_size=0.1 + (0.7*(j/50)), random_state=i)
        clf = SVC(kernel='rbf', gamma=0.01)
        clf.fit(X_train, y_train)
        SMOTE_test_error += 1 - clf.score(X_test, y_test)

        # Testing Neural Network
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1 + (0.7*(j/50)), random_state=i)
        clf = MLPClassifier(solver='lbfgs')
        clf.fit(X_train, y_train)
        NN_test_error += 1 - clf.score(X_test, y_test)

    Base_error[j] = base_test_error
    SMOTE_error[j] = SMOTE_test_error
    NN_error[j] = NN_test_error


plt.plot(test_size, Base_error, label="Base SVM")
plt.plot(test_size, SMOTE_error, label="SMOTE Augmented SVM")
plt.plot(test_size, NN_error, label="MLP Classifier")
plt.title("Percent Error for each Classifier for Varius Traning Dataset Sizes")
plt.xlabel("Proportion of Dataset as Test Data")
plt.ylabel("Test Error Percentage")
plt.legend()
plt.show()




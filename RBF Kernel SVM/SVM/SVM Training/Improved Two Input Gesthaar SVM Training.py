import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from micromlgen import port
from sklearn.model_selection import train_test_split

def haar_transform(x, n):
    y = []
    for i in range(0, int((n/2)-1)):
        y.append((x[2*i] + x[(2*i) + 1]) / 2)

    return y



results = []
with open("clockwise_circle_50.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

X_raw = np.zeros((100, 384))

for j in range(0, 50):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j][i%128] = results[i][0]
        X_raw[j][128 + (i%128)] = results[i][1]
        X_raw[j][256 + (i%128)] = results[i][2]

plt.plot(range(1, 129), X_raw[0][0:128], label="X")
plt.plot(range(1, 129), X_raw[0][128:256], label="Y")
plt.plot(range(1, 129), X_raw[0][256:384], label="Z")
plt.legend()
plt.show()

X = np.zeros((100, 93))
for i in range(0, 50):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)

plt.plot(range(1, 32), X[0][0:31], label="X")
plt.plot(range(1, 32), X[0][31:62], label="Y")
plt.plot(range(1, 32), X[0][62:93], label="Z")
plt.legend()
plt.show()




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


plt.plot(range(1, 129), X_raw[51][0:128], label="X")
plt.plot(range(1, 129), X_raw[51][128:256], label="Y")
plt.plot(range(1, 129), X_raw[51][256:384], label="Z")
plt.legend()
plt.show()

for i in range(50, 100):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)



plt.plot(range(1, 32), X[51][0:31], label="X")
plt.plot(range(1, 32), X[51][31:62], label="Y")
plt.plot(range(1, 32), X[51][62:93], label="Z")
plt.legend()
plt.show()

y = np.zeros(100)
y[50:100] = np.ones(50)

'''
clf = SVC(kernel='rbf', gamma=0.01)
clf.fit(X, y)
y_predict = clf.predict(X)
c_code = port(clf)
print(c_code)
'''

# Grid Search for best gamma and c

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
clf = SVC(kernel='rbf', gamma=0.5)
clf.fit(X_train, y_train)
train_error = 1 - clf.score(X_train, y_train)
print(train_error)
test_error = 1 - clf.score(X_test, y_test)
print(test_error)
#for i in range (1, 11):
#    for j in range (1, 11):













import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from micromlgen import port

def haar_transform(x, n):
    y = []
    for i in range(0, int((n/2)-1)):
        y.append((x[2*i] + x[(2*i) + 1]) / 2)

    return y



results = []
with open("clockwise_circle_15.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

X_raw = np.zeros((30, 384))

for j in range(0, 15):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j][i%128] = results[i][0]
        X_raw[j][128 + (i%128)] = results[i][1]
        X_raw[j][256 + (i%128)] = results[i][2]

plt.plot(range(1, 129), X_raw[0][0:128], label="X")
plt.plot(range(1, 129), X_raw[0][128:256], label="Y")
plt.plot(range(1, 129), X_raw[0][256:384], label="Z")
plt.legend()
plt.show()

X = np.zeros((30, 93))
for i in range(0, 15):
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
with open("counter_clockwise_circle_15.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

for j in range(0, 15):
    for i in range((128*j), ((128*j) + 128)):
        X_raw[j + 15][i%128] = results[i][0]
        X_raw[j + 15][128 + (i%128)] = results[i][1]
        X_raw[j + 15][256 + (i%128)] = results[i][2]


plt.plot(range(1, 129), X_raw[15][0:128], label="X")
plt.plot(range(1, 129), X_raw[15][128:256], label="Y")
plt.plot(range(1, 129), X_raw[15][256:384], label="Z")
plt.legend()
plt.show()

for i in range(15, 30):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)



plt.plot(range(1, 32), X[15][0:31], label="X")
plt.plot(range(1, 32), X[15][31:62], label="Y")
plt.plot(range(1, 32), X[15][62:93], label="Z")
plt.legend()
plt.show()

y = np.zeros(30)
y[15:30] = np.ones(15)


clf = SVC(kernel='rbf', C=8, gamma=0.5)
clf.fit(X, y)
y_predict = clf.predict(X)
c_code = port(clf)
print(c_code)



'''
print(results[0])
print(results[1])
print(results[0][0])
print(results[1][0])
x_coord = []
y_coord = []
z_coord = []
for i in range(0, len(results)):
    x_coord.append(results[i][0])
    y_coord.append(results[i][1])
    z_coord.append(results[i][2])

plt.plot(range(1, 129), x_coord, label="Orginal")
x_haar_1 = haar_transform(x_coord, 128)
plt.legend()
plt.show()
plt.plot(range(1, 64), x_haar_1, label="64 Features")
plt.legend()
plt.show()
x_haar_2 = haar_transform(x_haar_1, 64)
plt.plot(range(1, 32), x_haar_2, label="32 Features")
plt.legend()
plt.show()
x_haar_3 = haar_transform(x_haar_2, 32)
plt.plot(range(1, 16), x_haar_3, label="16 Features")
plt.legend()
plt.show()
'''
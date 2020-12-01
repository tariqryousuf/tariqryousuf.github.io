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


''''
plt.plot(range(1, 129), X_raw[15][0:128], label="X")
plt.plot(range(1, 129), X_raw[15][128:256], label="Y")
plt.plot(range(1, 129), X_raw[15][256:384], label="Z")
plt.legend()
plt.show()
'''


for i in range(0, 50):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)

'''
plt.plot(range(1, 32), X[15][0:31], label="X")
plt.plot(range(1, 32), X[15][31:62], label="Y")
plt.plot(range(1, 32), X[15][62:93], label="Z")
plt.legend()
plt.show()
'''

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

'''
plt.plot(range(1, 129), X_raw[50][0:128], label="X")
plt.plot(range(1, 129), X_raw[50][128:256], label="Y")
plt.plot(range(1, 129), X_raw[50][256:384], label="Z")
plt.legend()
plt.show()
'''

for i in range(50, 100):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


'''
plt.plot(range(1, 32), X[50][0:31], label="X")
plt.plot(range(1, 32), X[50][31:62], label="Y")
plt.plot(range(1, 32), X[50][62:93], label="Z")
plt.legend()
plt.show()
'''




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


'''
plt.plot(range(1, 129), X_raw[100][0:128], label="X")
plt.plot(range(1, 129), X_raw[100][128:256], label="Y")
plt.plot(range(1, 129), X_raw[100][256:384], label="Z")
plt.legend()
plt.show()
'''

for i in range(100, 150):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


'''
plt.plot(range(1, 32), X[100][0:31], label="X")
plt.plot(range(1, 32), X[100][31:62], label="Y")
plt.plot(range(1, 32), X[100][62:93], label="Z")
plt.legend()
plt.show()
'''


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

'''
plt.plot(range(1, 129), X_raw[152][0:128], label="X")
plt.plot(range(1, 129), X_raw[152][128:256], label="Y")
plt.plot(range(1, 129), X_raw[152][256:384], label="Z")
plt.legend()
plt.show()
'''

for i in range(150, 200):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


'''
plt.plot(range(1, 32), X[152][0:31], label="X")
plt.plot(range(1, 32), X[152][31:62], label="Y")
plt.plot(range(1, 32), X[152][62:93], label="Z")
plt.legend()
plt.show()
'''


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


'''
plt.plot(range(1, 129), X_raw[201][0:128], label="X")
plt.plot(range(1, 129), X_raw[201][128:256], label="Y")
plt.plot(range(1, 129), X_raw[201][256:384], label="Z")
plt.legend()
plt.show()
'''

for i in range(200, 250):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


'''
plt.plot(range(1, 32), X[201][0:31], label="X")
plt.plot(range(1, 32), X[201][31:62], label="Y")
plt.plot(range(1, 32), X[201][62:93], label="Z")
plt.legend()
plt.show()
'''




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


'''
plt.plot(range(1, 129), X_raw[251][0:128], label="X")
plt.plot(range(1, 129), X_raw[251][128:256], label="Y")
plt.plot(range(1, 129), X_raw[251][256:384], label="Z")
plt.legend()
plt.show()
'''

for i in range(250, 300):
    x_haar_1 = haar_transform(X_raw[i][0:128], 128)
    X[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw[i][128:256], 128)
    X[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw[i][256:384], 128)
    X[i][62:93] = haar_transform(z_haar_1, 64)


'''
plt.plot(range(1, 32), X[251][0:31], label="X")
plt.plot(range(1, 32), X[251][31:62], label="Y")
plt.plot(range(1, 32), X[251][62:93], label="Z")
plt.legend()
plt.show()
'''

y = np.zeros(300)
y[50:100] = np.ones(50)
y[100:150] = np.full(50, 2)
y[150:200] = np.full(50, 3)
y[200:250] = np.full(50, 4)
y[250:300] = np.full(50, 5)

clf = SVC(kernel='rbf', gamma=0.01)
clf.fit(X, y)
y_predict = clf.predict(X)
c_code = port(clf)
print(c_code)





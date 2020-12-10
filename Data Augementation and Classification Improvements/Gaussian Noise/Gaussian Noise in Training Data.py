import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from micromlgen import port
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import ADASYN

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


X_noise = np.zeros((300, 93))
for i in range(0, 300):
    x_haar_1 = haar_transform(X_raw_noise[i][0:128], 128)
    X_noise[i][0:31] = haar_transform(x_haar_1, 64)
    y_haar_1 = haar_transform(X_raw_noise[i][128:256], 128)
    X_noise[i][31:62] = haar_transform(y_haar_1, 64)
    z_haar_1 = haar_transform(X_raw_noise[i][256:384], 128)
    X_noise[i][62:93] = haar_transform(z_haar_1, 64)


plt.plot(range(1, 32), X_noise[0][0:31], label="X")
plt.plot(range(1, 32), X_noise[0][31:62], label="Y")
plt.plot(range(1, 32), X_noise[0][62:93], label="Z")
plt.legend()
plt.show()


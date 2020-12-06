import csv
import numpy as np
import matplotlib.pyplot as plt

def haar_transform(x, n):
    y = []
    for i in range(0, int((n/2)-1)):
        y.append((x[2*i] + x[(2*i) + 1]) / 2)

    return y


def non_linear_quantization(a):
    if (abs(a) < 0.05):
        return_value = 0
    elif (abs(a) < 1.0):
        if (a > 0.0):
            return_value = (int((a + 0.1) * 10))
        else:
            return_value = (int((a - 0.1) * 10))
    elif ((a > 0.0)):
        if (abs(a) < 1.2):
            return_value = 11
        elif (abs(a) < 1.4):
            return_value = 12
        elif (abs(a) < 1.6):
            return_value = 13
        elif (abs(a) < 1.8):
            return_value = 14
        elif (abs(a) < 2.0):
            return_value = 15
        else:
            return_value = 16
    else:
        if (abs(a) < 1.2):
            return_value = -11
        elif (abs(a) < 1.4):
            return_value = -12
        elif (abs(a) < 1.6):
            return_value = -13
        elif (abs(a) < 1.8):
            return_value = -14
        elif (abs(a) < 2.0):
            return_value = -15
        else:
            return_value = -16

    return return_value

results = []
with open("left_arrow_2.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

X_raw = np.zeros((1, 384))
for i in range(0, 128):
    X_raw[0][i%128] = results[i][0]
    X_raw[0][128 + (i%128)] = results[i][1]
    X_raw[0][256 + (i%128)] = results[i][2]



X = np.zeros((1, 93))
x_haar_1 = haar_transform(X_raw[0][0:128], 128)
X[0][0:31] = haar_transform(x_haar_1, 64)

y_haar_1 = haar_transform(X_raw[0][128:256], 128)
X[0][31:62] = haar_transform(y_haar_1, 64)

z_haar_1 = haar_transform(X_raw[0][256:384], 128)
X[0][62:93] = haar_transform(z_haar_1, 64)

X_q = np.zeros((1, 93))
for i in range(0, 93):
    X_q[0][i] = non_linear_quantization(X[0][i])

plt.plot(range(1, 32), X_q[0][0:31], label="X")
plt.plot(range(1, 32), X_q[0][31:62], label="Y")
plt.plot(range(1, 32), X_q[0][62:93], label="Z")
plt.legend()
plt.show()



for i in range(0, 31):
    #print("{" + str(int(results[i][0])) + ", " + str(int(results[i][1])) + ", " + str(int(results[i][2])) + "},")
    print("{" + str(int(X_q[0][i])) + ", " + str(int(X_q[0][i + 31])) + ", " + str(int(X_q[0][i + 62])) + "},")



'''
for i in range(len(results)):
    #print("{" + str(int(results[i][0])) + ", " + str(int(results[i][1])) + ", " + str(int(results[i][2])) + "},")
    print("{" + str(non_linear_quantization(results[i][0])) + ", " + str(non_linear_quantization(results[i][1])) + ", " + str(non_linear_quantization(results[i][2])) + "},")
'''

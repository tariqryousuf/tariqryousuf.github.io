from sklearn.svm import SVC
from micromlgen import port
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target
clf = SVC(kernel='rbf', gamma=0.001)
clf.fit(X, y)
y_predict = clf.predict(X)
c_code = port(clf)
print(c_code)
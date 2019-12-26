# randomforest over the digits dataset, the toy data that we used for many examples earlier in this book.
# the randomforest algorithm below frequently achieves an accuracy score of 1.


import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale

digits = load_digits()
data = scale(digits.data)

n_samples, n_features = data.shape
n_digits = len(np.unique(digits.target))
labels = digits.target

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(data, labels)
scores = clf.score(data,labels)
print(scores)

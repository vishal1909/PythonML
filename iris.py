#!/usr/bin/python3
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

iris=load_iris()
columns=dir(load_iris())
print(columns)
input=iris.data
output=iris.target
feature=iris.feature_names
target=iris.target_names
print(input)
print(output)
print(feature)
print(target)
ishape=input.shape
oshape=output.shape

print(ishape)
print(oshape)

x=[0,50,100]
train_data=np.delete(iris.data,x,axis=0)
train_target=np.delete(iris.target,x)
test_data=iris.data[x]
algo=tree.DecisionTreeClassifier()
trained=algo.fit(train_data,train_target)
predict=trained.predict(test_data)
print(predict)




#!/usr/bin/python3

import sklearn
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_diabetes 
import numpy as np



"""
load=load_diabetes()
train_data=np.delete(load.data,1,axis=0)
train_target=np.delete(load.target,1)
clf=tree.DecisionTreeClassifier()
algo=clf.fit(train_data,train_target)
out=algo.predict([load.data[1]])
print(out)

"""





from sklearn.model_selection import train_test_split

iris=load_iris()  # loading dataset



#train_data,test_data,train_target,test_target=train_test_split  (training and testing)
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.03)

#  calling  decisiontree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target) # training data
output=trained.predict(test_data)
print(output) #predicted output
print(test_target) #exact output

from  sklearn.metrics  import  accuracy_score
x=accuracy_score(test_target,output)
print("Accuracy is",x)

print("DIABETES")
load=load_diabetes()
train_data,test_data,train_target,test_target=train_test_split(load.data,load.target,test_size=0.03)

cf=tree.DecisionTreeClassifier()
algo=cf.fit(train_data,train_target)
out=algo.predict(test_data)
print(out)
print(test_target)

y=accuracy_score(test_target,out)
print("Accuracy is",y)

"""
import matplotlib.pyplot as mp
q=["iris","diabetes"]
e=[x,y]
mp.bar(q,e)
mp.show()

"""

tree.export_graphviz(clf, out_file="treeiris.dot", max_depth=4,feature_names=iris.feature_names, class_names=iris.target_names, filled=True , rounded=True )













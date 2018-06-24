#!/usr/bin/python2


import os
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import load_wine

wine=load_wine()
#print(wine)
train_data,test_data,train_target,test_target=train_test_split(wine.data,wine.target,test_size=0.05)
print("Decision Tree Classifier")
#  calling  decisiontree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
#  predicting output 
predicted=trained.predict(test_data)

print(predicted)
#  now calculating  accuracy 
from  sklearn.metrics  import  accuracy_score

pct=accuracy_score(test_target,predicted)
print(pct)

from sklearn.neighbors import KNeighborsClassifier
print("K nearest classifier")
kclf=KNeighborsClassifier(n_neighbors=3)
train=kclf.fit(train_data,train_target)
predict=train.predict(test_data)
print (predict)
accuracy=accuracy_score(test_target,predict)
print(accuracy)

print("Support Vector Machine Algorithm")
from sklearn.svm import SVC
classify=SVC()
train=classify.fit(train_data,train_target)
result=train.predict(test_data)
print(result)

score=accuracy_score(test_target,result)
print(score)
print("Naive Bayes Algorithm")
from sklearn.naive_bayes  import GaussianNB
bayes=GaussianNB()
trained=bayes.fit(train_data,train_target)
outcome=trained.predict(test_data)
print(outcome)

out=accuracy_score(test_target,outcome)
print(out)



import numpy as np
print("Algorithm Comparison")
cmp=np.array([pct,out,score,accuracy])
cmp.max()
if cmp.max()==pct:
	print("best algo is decision tree",+cmp.max())
elif cmp.max()==out:
	print("best algo is naive bayes tree",+cmp.max())
elif cmp.max()==score:
	print("best algo is Support Vector Machine",+cmp.max())
else:
	print("best algo is K nearest neighbors",+cmp.max())



















#!/usr/bin/python3
import time
#import matplotlib.pyplot as plt
from sklearn.datasets  import load_iris
from  sklearn  import  tree

#from  sklearn.cross_validation  import  train_test_split

from   sklearn.model_selection  import  train_test_split
#  loading  iris
iris=load_iris()


train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.1)

#  calling  decisiontree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target)
#  predicting output 
predicted=trained.predict(test_data)

#print(predicted)
#  now calculating  accuracy 
from  sklearn.metrics  import  accuracy_score

pct=accuracy_score(test_target,predicted)
print(pct)


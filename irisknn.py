#!/usrbin/python3

import sklearn
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris=load_iris()  # loading dataset



#train_data,test_data,train_target,test_target=train_test_split  (training and testing)
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.2)

#  calling  decisiontree
clf=tree.DecisionTreeClassifier()
trained=clf.fit(train_data,train_target) # training data
output=trained.predict(test_data)
print(output) #predicted output
print(test_target) #exact output

from  sklearn.metrics  import  accuracy_score

print("Accuracy is",accuracy_score(test_target,output))

print("K nearest neighbor algorithm")

#calling knn classifier
#neigh=int(input("No.of neighbors"))
kclf=KNeighborsClassifier(n_neighbors=10)
train=kclf.fit(train_data,train_target)
predict=train.predict(test_data)
print(predict) #predicted output
print(test_target) #exact output

from  sklearn.metrics  import  accuracy_score

print("Accuracy is",accuracy_score(test_target,predict))











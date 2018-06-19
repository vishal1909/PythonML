
# coding: utf-8

# In[25]:


#!/usrbin/python3

import sklearn
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from  sklearn.metrics  import  accuracy_score

iris=load_iris()  # loading dataset

print("ALGORITHMS COMPARISON")
test_size=range(1,5)
out=[]
#train_data,test_data,train_target,test_target=train_test_split  (training and testing)
for size in test_size:
        train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=size/10)


#  calling  decisiontree
        clf=tree.DecisionTreeClassifier()
        trained=clf.fit(train_data,train_target) # training data
        output=trained.predict(test_data)
        p=accuracy_score(test_target,output)
        out.append(p)
#print(output) #predicted output
#print(test_target) #exact output





#print("K nearest neighbor algorithm")

#calling knn classifier
#neigh=int(input("No.of neighbors"))
krange=range(1,10)
score=[]
for k in krange:
        kclf=KNeighborsClassifier(n_neighbors=k)
        train=kclf.fit(train_data,train_target)
        predict=train.predict(test_data)
        x=accuracy_score(test_target,predict)
        score.append(x)    
    
    
import matplotlib.pyplot as mp
mp.xscale("linear")
mp.yscale("linear")
mp.xlabel("values of k ->")
mp.ylabel("percentage of accuracy (by 100)")
mp.title("K Nearest Neighbor algorithm")
mp.grid(color="yellow")
mp.plot(krange,score,color="blue")
mp.show()
mp.title("Decision Tree clasiifier algorithm")
mp.xlabel("values of test splitting ->")
mp.ylabel("percentage of accuracy (by 100)")
mp.xscale("linear")
mp.yscale("linear")
mp.grid(color="yellow")
mp.plot(test_size,out,color="red")
mp.show()

#print("Accuracy is",accuracy_score(test_target,predict))










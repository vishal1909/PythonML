
# coding: utf-8

# In[2]:


import matplotlib.pyplot as mp
x=[1,2,3]
y=[3,4,5]
mp.plot(x,y)
mp.show()


# In[3]:


import matplotlib.pyplot as mp
x=[1,2,3]
y=[3,4,5]
mp.xlabel("time")
mp.ylabel("speed")
mp.plot(x,y)
mp.show()


# In[5]:


import matplotlib.pyplot as mp
x=[1,2]
y=[3,4]
mp.xlabel("time")
mp.ylabel("speed")
mp.plot(x,y,label="flyover")
mp.legend()
mp.grid(color="green")
mp.show()


# In[11]:


import matplotlib.pyplot as mp
q=[6,7,8]
e=[4,5,6]
x=[1,2,3]
y=[3,4,5]
mp.scatter(x,y,label="mines" , marker="x", color='black')
mp.plot(q,e,label="road", color="red")
mp.grid(color="yellow")
mp.legend()
mp.show()


# In[14]:


import matplotlib.pyplot as mp
x=["north","west","east","south"]
y=[20,12,35,43]
mp.xlabel("Direction")
mp.ylabel("Population(in lakhs)")
mp.bar(x,y,color="pink")

mp.show()


# In[19]:


import matplotlib.pyplot as mp
x=[1,2,3]
y=[3,4,5]
mp.title("Scaling Graph")
mp.xscale("linear")
mp.yscale("log")
mp.plot(x,y)
mp.show()


# In[29]:


#Some advanced options
a=([4,1,7,3,2,5,9,0])

b=sorted(a)
print (b)


# In[30]:


a=([1,1,6,4,2,3,6,2,7,9,5,2,4])
a.count(2)


# In[31]:


a.count(1)


# In[32]:


a.count(5)


# In[33]:


a.index(1)


# In[34]:


a.index(4)


# In[ ]:





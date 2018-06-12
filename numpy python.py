
# coding: utf-8

# In[1]:


import numpy


# In[4]:


a = numpy.array([1,2,3,4])


# In[5]:


a


# In[6]:


a[2]


# In[7]:


b=numpy.array([2,4,6,7])


# In[8]:


b


# In[9]:


b[3]


# In[11]:


c=a+b


# In[12]:


c


# In[17]:


f=numpy.mat(("1,2,3;4,5,6;7,8,9"))


# In[18]:


f


# In[19]:


g=numpy.mat(("1,20,4;4,518,6;76,81,9"))


# In[20]:


g


# In[21]:


h=f+g


# In[22]:


h


# In[25]:


a=numpy.array([[1,2,3],[2,4,5],[1,6,7]])


# In[26]:


a


# In[27]:


b=numpy.array([[11,2,23],[21,49,5],[10,6,71]])


# In[28]:


b


# In[29]:


c=a+b


# In[30]:


c


# In[31]:


a.shape


# In[32]:


b.shape


# In[36]:


c.shape


# In[35]:


b.dtype


# In[37]:


c.dtype


# In[38]:


w=numpy.array([1.0,2.0,3.0])


# In[39]:


w


# In[40]:


w.dtype


# In[41]:


f.dtype


# In[54]:


numpy.arange(6) #creating a 1D array


# In[50]:


dd=numpy.arange(8)


# In[51]:


dd


# In[52]:


numpy.arange(6).reshape(2,3) #reshaping


# In[53]:


numpy.arange(6).reshape(3,2)


# In[55]:


numpy.ones((3,2))# fill ones in matrix of given size


# In[57]:


numpy.zeros((3,2)) # fill zeoes in matrix of given size


# In[59]:


numpy.random.random((1,1)) # random values stored in array


# In[62]:


numpy.eye((3)) # form a identity matrix


# In[67]:


numpy.full((1,3),4) #to fill the complete array with number 4


# In[68]:


numpy.eye((4))


# In[70]:


numpy.arange(10)**2


# In[72]:


qw=numpy.arange(10)**2


# In[73]:


qw


# In[74]:


numpy.sqrt(qw)


# In[75]:


numpy.add(a,b)


# In[76]:


numpy.add(qw,qw)


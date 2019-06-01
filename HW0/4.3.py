
# coding: utf-8

# In[28]:


import numpy as np

A = np.array([[1,4,-3],[2,-1,3]])
B = np.array([[-2,0,5],[0,-1,4]])


# In[29]:


##np.dot(A,B)


# In[30]:


np.dot(A.T,B)


# In[31]:


np.linalg.matrix_rank(np.dot(A.T,B))


# In[32]:


C = np.array([[1,0],[0,2]])

np.dot(A,B.T)+C^-1


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = [[26,64,5,92],[63,19,4,50],[76,23,97,49],[11,16,77,92],[73,48,62,51],[12,38,38,94],[83,96,93,70],[4,49,19,1],[71,63,40,57],[22,82,56,19],[64,100,24,19],[14,22,29,28],[84,33,70,0],[62,37,99,76],[80,74,81,15],[95,25,64,77],[19,21,2,90],[80,29,50,24],[8,27,8,72],[10,58,68,70],[67,5,73,26],[65,60,75,16],[15,91,6,49],[75,29,42,98],[34,17,29,26],[86,18,18,66],[3,48,69,9],[0,77,63,50],[13,67,23,3],[8,55,12,22],[49,72,69,59],[72,19,56,91],[29,86,20,16],[5,19,30,13],[26,33,96,62],[87,5,61,29],[94,38,9,83],[60,89,65,87],[71,31,100,16],[20,95,66,78],[90,32,23,68],[43,38,6,97],[30,10,85,49],[49,67,37,80],[89,60,62,93],[27,88,95,81],[59,0,31,69],[14,78,30,88],[54,59,91,10],[8,35,100,1],[9,38,71,48],[9,9,45,67],[85,15,35,30],[19,98,54,12],[84,47,61,46],[53,22,0,7],[5,95,69,45],[17,14,92,43],[81,91,29,44],[68,27,45,29],[88,2,38,21],[6,62,10,36],[86,31,5,84],[19,73,74,79],[21,57,49,86],[44,7,49,30],[7,99,78,59],[38,0,65,25],[13,77,63,64],[39,2,73,17],[93,86,34,96],[42,60,84,98],[10,39,66,81],[42,14,66,80],[37,70,42,14],[69,86,68,47],[0,14,51,10],[5,39,73,63],[15,58,49,52],[54,75,5,32],[36,29,61,21],[31,42,17,91],[83,45,8,46],[87,84,82,68],[48,77,14,87],[80,54,57,21],[4,32,50,8],[85,87,14,96],[63,19,17,44],[78,16,52,27],[74,53,57,27],[79,85,87,48],[98,50,53,60],[14,90,21,11],[22,67,25,75],[77,32,52,49],[43,9,1,61],[88,27,50,3],[51,85,18,88],[95,35,9,22]]
y = [1272,2402,4258,3054,3113,2019,3328,-541,2484,273,579,969,2862,4103,2420,4727,1864,2947,1183,1625,3520,2202,-364,4094,1601,3615,481,479,-519,-237,2245,4308,-264,524,2890,3944,3602,2670,3375,1254,3552,2384,3024,2185,4097,2154,3503,1017,2081,1244,1614,2123,3239,-262,3333,1171,278,2562,1765,2683,3451,-204,3487,1828,1926,2498,669,2645,1112,2634,3289,3260,2164,3518,600,2278,781,1785,1078,718,1876,2036,2424,3456,1713,2523,486,2714,2524,3253,2510,2886,3777,-850,1122,3350,2184,2828,1692,2548]
x = np.array(x)
y = np.array(y)
y = y.reshape(100,1)


# In[3]:


random_init = np.random.randn(5)
weights = random_init[:4].reshape(-1,1)
bias = random_init[4]
weights_1 = weights + 0.1


# In[4]:


weights


# In[5]:


error1 = list()
for i in range(10000):
    y_pred = np.matmul(x, weights) + bias
    y_diff = y - y_pred
    derivative = -2 * np.matmul(x.T, y_diff)/100
    derivative_bias = -2 * y_diff.sum()/100
    error = np.matmul(y_diff.T,y_diff)/100
    error1.append(error)
    derivative2 = np.array([np.matmul(x[:,0].T,x[:,0]),np.matmul(x[:,1].T,x[:,1]),np.matmul(x[:,2].T,x[:,2]),np.matmul(x[:,3].T,x[:,3])]).reshape(4,1) *2 /100
    weights -= derivative * 0.000001
    bias -= derivative_bias * 0.000001
    print(f"The iteration number is {i}, error is {error}")


# In[6]:


import matplotlib.pyplot as plt


# In[7]:


error1 = np.array(error1).reshape(10000,1)


# In[8]:


plt.plot(error1)
plt.grid()
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.show()


# In[9]:


weights


# In[ ]:





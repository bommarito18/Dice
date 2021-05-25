#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd


# In[16]:


die = pd.DataFrame([1, 2, 3, 4, 5, 6])
sum_of_dice = die.sample(2, replace=True).sum().loc[0]
print('Sum of dice is', sum_of_dice)


# In[17]:


trial = 1000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]


# In[18]:


print(results[:10000])


# In[19]:


freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()
sort_freq


# In[20]:


relative_freq=sort_freq/sort_freq.sum()
relative_freq.plot(kind='bar', color='blue')


# In[21]:


X_distri = pd.DataFrame(index=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
X_distri['Prob'] = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
X_distri['Prob'] = X_distri['Prob']/36
X_distri


# In[ ]:





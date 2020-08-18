#!/usr/bin/env python
# coding: utf-8

# #### Mcdonald Assignment:

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
get_ipython().run_line_magic('matplotlib', 'inline')
import statsmodels.api as sm
import scipy.stats as stats 
import copy 
import os


# In[2]:


a=pd.read_csv('Mcdonald .csv')
a


# #### Plot graphically which food categories have the highest and lowest varieties.

# In[3]:


#ans
b=a.Category.value_counts().plot(kind='barh')
b


# In[4]:


a


# #### Which all variables have an outlier?

# In[5]:


#ans
cols=['Calories',                         
    'Calories from Fat',              
    'Total Fat',                      
    'Total Fat (% Daily Value)',        
    'Saturated Fat',                  
    'Saturated Fat (% Daily Value)',   
    'Trans Fat',                      
   'Cholesterol',                    
   'Cholesterol (% Daily Value)',      
   'Sodium',                          
   'Sodium (% Daily Value)',           
   'Carbohydrates',                    
   'Carbohydrates (% Daily Value)',    
   'Dietary Fiber',                    
   'Dietary Fiber (% Daily Value)',   
   'Sugars',                           
   'Protein',                         
   'Vitamin A (% Daily Value)',        
   'Vitamin C (% Daily Value)',       
   'Calcium (% Daily Value)',         
   'Iron (% Daily Value)']
plt.figure(figsize=[25,25])
for i in range(len(cols)):
    plt.subplot(6,4,i+1)
    sns.boxplot(a[cols[i]])


# #### Which variables have the highest correlation? Plot them and find out the value?

# In[6]:


#ans
c=a[['Calories',                         
    'Calories from Fat',              
    'Total Fat',                      
    'Total Fat (% Daily Value)',        
    'Saturated Fat',                  
    'Saturated Fat (% Daily Value)',   
    'Trans Fat',                      
   'Cholesterol',                    
   'Cholesterol (% Daily Value)',      
   'Sodium',                          
   'Sodium (% Daily Value)',           
   'Carbohydrates',                    
   'Carbohydrates (% Daily Value)',    
   'Dietary Fiber',                    
   'Dietary Fiber (% Daily Value)',   
   'Sugars',                           
   'Protein',                         
   'Vitamin A (% Daily Value)',        
   'Vitamin C (% Daily Value)',       
   'Calcium (% Daily Value)',         
   'Iron (% Daily Value)']].corr()
c


# In[7]:


plt.figure(figsize=[30,30])
d=sns.heatmap(c,annot=True)
d


# #### Which category contributes to the maximum % of Cholesterol in a diet (% daily value)?

# In[8]:


#ans
a.groupby('Category')['Cholesterol (% Daily Value)'].describe().sort_values(by='mean',ascending=False).head()


# #### Which item contributes maximum to the Sodium intake?

# In[9]:


#ans
a.groupby('Item')['Sodium'].describe().sort_values(by='mean',ascending=False).head()


# #### Which 4 food items contain the most amount of Saturated Fat?

# In[10]:


#ans
a.groupby('Item')['Saturated Fat'].describe().sort_values(by='mean',ascending=False).head()


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import dependencies 


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# Load data 


# In[2]:


df = pd.read_csv('tcs.csv')
df


# In[ ]:





# In[3]:


# set the index

df= df.set_index(pd.DatetimeIndex(df['Date']))

df


# In[5]:


#visualize

plt.figure(figsize=(12.2,4.5))
plt.title('Share Price', fontsize= 20)
plt.plot(df['Close'])
plt.xlabel("Date", fontsize= 20)
plt.ylabel("Share Price" , fontsize= 20)

plt.show()


# ## calculate the three moving average

# #### calculate short/fast moving average

# In[6]:


shortEMA= df.Close.ewm(span=5, adjust=False).mean()


# #### calculate middle/Medium moving average

# In[7]:


mediumEMA= df.Close.ewm(span=12 , adjust=False).mean()


# #### calculate Long/slow moving average

# In[8]:


longEMA= df.Close.ewm(span=21, adjust=False).mean()


# In[9]:


plt.figure(figsize=(12.2,4.5))
plt.title('Share Price',fontsize= 20)
plt.plot(df['Close'])
plt.plot(shortEMA, label= 'Short/Fast')
plt.plot(mediumEMA, label= 'Medium')
plt.plot(longEMA, label = 'Fast')
plt.xlabel("Date", fontsize= 20)
plt.ylabel("Share Price" , fontsize= 20)

plt.show()


# #### add exponential moving average to the data set

# In[10]:



df['Short']  =shortEMA
df['Middle'] =mediumEMA
df['Long'] = longEMA


# In[11]:


df


# #### creating function to buy and sell the stock

# In[13]:



def buy_sell_funt(data):
       buy_list =[]
       sell_list = []
       flag_long = False
       flag_short= False
       
       for i in range(0, len(data)):
           
           if data['Middle'][i]< data['Long'][i] and data['Short'][i]< data['Middle'][i] and flag_long == False and flag_short == False:
               buy_list.append(data['Close'][i])
               sell_list.append(np.nan)
               flag_short =True
               
           elif flag_short == True and data['Short'][i] > data['Middle'][i]:
               sell_list.append(data['Close'][i])
               buy_list.append(np.nan)
               flag_short == False
               
               
               
           elif data['Middle'][i] > data['Long'][i] and data['Short'][i]> data['Middle'][i] and flag_long == False and flag_short == False:
               buy_list.append(data['Close'][i])
               sell_list.append(np.nan)
               flag_long =True
               
           elif flag_long == True and data['Short'][i] < data['Middle'][i]:
               sell_list.append(data['Close'][i])
               buy_list.append(np.nan)
               flag_long ==False
               
           else:
               
               buy_list.append(np.nan)
               sell_list.append(np.nan)
               
       return (buy_list, sell_list)        


# ### Add buy sell signals to the data set
# 

# In[14]:


df['Buy'] = buy_sell_funt(df)[0]

df['Sell'] = buy_sell_funt(df)[1]


# In[15]:


plt.figure(figsize=(12.2,4.5))
plt.title('Buy and sell Plot of TCS Shares',fontsize= 20)
plt.plot(df['Close'], label= 'Close Price', color = 'blue', alpha = 0.35)
plt.plot(shortEMA, label= 'Short/Fast', color = 'red', alpha = 0.35)
plt.plot(mediumEMA, label= 'Medium', color = 'orange', alpha = 0.35)
plt.plot(longEMA, label = 'Fast')

plt.scatter(df.index,df['Buy'],color= 'green', marker= '^', alpha= 1 )

plt.scatter(df.index,df['Sell'],color= 'red', marker= 'v', alpha= 1 )

plt.xlabel("Date", fontsize= 20)
plt.ylabel("Share Price" , fontsize= 20)

plt.show()


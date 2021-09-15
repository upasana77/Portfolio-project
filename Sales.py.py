#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#so like amazon,flipkart companies are sailing lakhs of product, so we can think how much huge amount of data,
#these companies are creating,now the question is what type of data they are creating, let's say a customer
# i.e going to buy a product, will have a order ID, Product Name, Quantity of product, Price of product,
# purchase adress and many more attributes.so that type of data the person is going to produce.so as a data analyst,
# we have to analyse these data,so let's say I kave to analyse what are my most sold products?
# we can visualise it through a pie-chart that which product is my most sold product,or let's say I will have
# to analyse in which months my earning were best? for this we can create a bar chart to visualise our data,or 
# with the bar graph, we could conclude in which city, the company has maximum sale.so that is 
# basically the rough idea of what type of analysis we can perform on this sales data.


# In[ ]:


# so i have my sales data for each and every month, so my assignment for this sales data is : 
# I have to do data prepration


# In[6]:


# here I am going to import my panda,so that i can read and manipulate my data.
# I am going to import numpy to do some numerical task
# and for visualization , I am going to import my matplotlib. and will execute all the import librery.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[7]:


# As we have multiple datasets to work with,so I am going to combine all the files,so basically, 
#I need some of the advanced libraries,and some advanced function to combine,and then I have to read the combine file.
#so the library that I need is 'os' librery, so os is my operating system.so whenever we have to create some 
# folder or directory or we have to remove the directory,or we have to do some modification,or we have to 
# make a directory, in such case,we have to deal with this os librery.after importing the li brery, I can fetch 
# all the files available in this particular location. after importing the 'os'librery we can fetch all the files
# or more than one file together,so now I am going to copy the path,in my following statement I have passed my entire
# path,if we execute the following statement, as we can see we have all the listed files in the given folder.
# So that's the beauty of the os librery,so 'listdir' means a list of all the files available at tahat path.
# so I am just going to iterate over the list of files by appling a for loop,
# so now I am going to use my list comprehension, where I am going to append each and every file in my list,
# and finally i will store everything with a variable name Files,so I want to print my each file.
# so it will give me my all files


# In[8]:


files=[file for file in os.listdir('/Users/upasanapurohit/Desktop/Sales-Data')]
for file in files:
    print(file)


# In[9]:


# now I have to read all these files,so basically I can combine all these files, and then I can read it,
# instead of reading one by one,for this I am going to declare my blank data-frame, I am going to concatenate, my all
# files into 'all_data'.Then I am going to iterate over my list which is my files here,where I have to read each
# and every file, as I have to read, I have define my path, and 'current_df' is my data frame name
# ,now I have to concatenate the 'current_df' dataframe with the 'all_data' blank data-frame,So I am going to say
# pd.concate, and will pass my both data-frame un the form of list, and now I will update, as 'all_data'
# all_data.shape where I will check the shape of my data_frame


# In[10]:


path = ('/Users/upasanapurohit/Desktop/Sales-Data')
all_data = pd.DataFrame()
for file in files:
    current_df=pd.read_csv(path+"/"+file)
    all_data= pd.concat([all_data,current_df])
all_data.shape


# In[ ]:


# let's say I have to convert the Data_Frame to a csv file,and In the argument I will pass, the path where I will
# have to save the data,and I am going to set my index as false because I do not want index of my data,
# so if I will execute the statement it will covert all the data_frame into csv with the given particulaar location.or
# in my own path.


# In[11]:


all_data.to_csv('/Users/upasanapurohit/Desktop/Sales-Data/all_data.csv',index=False)


# In[ ]:





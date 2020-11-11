#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Standards
import pandas as pd
import numpy as np

# API
import requests

# Automating
import time
import datetime
import warnings
import sys


# In[22]:


def get_posts(subreddit, n_iter, epoch_right_now): # subreddit name and number of times function should run
    pass
    # store base url variable
    base_url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='
    
    # instantiate empty list    
    df_list = []
    
    # save current epoch, used to iterate in reverse through time
    current_time = epoch_right_now
    
    # set up for loop
    for post in range(n_iter):
        
        # instantiate get request
        res = requests.get(
            
            # requests.get takes base_url and params
            base_url,
            
            # parameters for get request
            params = {  
                
                # specify subreddit
                'subreddit': subreddit,
                
                # specify number of posts to pull
                'size': 100,
                
                # ???
                'lang': True,
                
                # pull everything from current time backward
                'before': current_time }
        )
        
        # take data from most recent request, store as df
        df = pd.DataFrame(res.json()['data'])
        
        # pull specific columns from dataframe for analysis
        df = df.loc[:, ['title',
                'created_utc',
                'selftext',
                'subreddit',
                'author',
                'media_only',
                'permalink']]
        
        # append to empty dataframe list
        df_list.append(df)
        
        # add wait time - seconds in parentheses
        time.sleep(30)
        
        # set current time counter back to last epoch in recently grabbed df
        current_time = df['created_utc'].min()

    # return one dataframe for all requests
    return pd.concat(df_list, axis=0)

# Adapated from Tim Book's Lesson Example


# In[23]:


legal = get_posts('legaladvice',300, 1601524444)

# In[25]:


nsq = get_posts('NoStupidQuestions',300,1601524444)


# In[1]:


legal_nsq = pd.concat([legal, nsq])


# In[ ]:


legal_nsq.to_csv('legal_nsq.csv', index=False)


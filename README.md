# Project 3: Reddit NLP

### Problem Statement

Reddit calls itself the front page of the internet. Reddit is made up of several internet communities called subreddits. One very popular use of Reddit is asking questions. The Legal Advice subreddit (r/legaladvice) is a community for asking basic legal questions and the explanation of basic legal concepts. No Such Thing as Stupid Questions subreddit (r/nostupidquestions) is a judgement-free zone for all of the questions that you may be too embarassed to ask. Both of these subreddits are communities for users who have questions that they feel most comfortable turning to the internet to. This project will combine web scraping using an API, Natural Language Processing, and classification modeling to determine which subreddit is the origin of each post. 


### Executive Summary

To address this problem, I begin by using the Pushshift API to pull 30,000 submission from each subreddit. Next, I inspect and clean the data to address removed posts, missing values, and duplicates, as well as special characters and text features. Then I use the cleaned data to begin exploratory data analysis. Here, I assess word counts for each subreddit, using both the title data and the title and text combined. I will also use sentiment analysis to look for key differences, as well as word frequency by subreddit.

After data collection, cleaning, and EDA, I will begin building models. First I will use a Multinomial Naive Bayes, utilizing gridsearch to determine the best parameters using both CountVectorizer and TfidfVectorizer as preprocessors. Here, the CountVectorizer performs best, with a test accuracy score of 0.93. Next, I will run seven different models using their base parameters in order to identify two models for additional tuning: Logistic Regression and Random Forest.  The advantage to a Logistic Regression model is the interpretability of coefficients.  

In conclusion, I determine that the Logistic Regression model is best suited for this problem, due to accuracy scores and interpretability.


### Contents
- 01 Data Collection
- 02 Data Cleaning 
- 03 EDA
- 04 Model 1 - Multinomial Naive Bayes
- 05 Model 2 - Additional Modeling
- Data
 - legal_nsq.csv
 - legal_nsq_clean.csv

### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|title|object|Title of submission post|
|created_utc|int64|Epoch time of post|
|selftext|object|Body text of submission post|
|subreddit|object|Name of the subreddit (target)|
|author|object|Username of the submission post's author|
|media_only|bool|Boolean value, indicates whether a post is media only|
|permalink|object|extension of the URL|
|clean_text|object|A RegEx-cleaned version of selftext column|
|clean_title|object|A RegEx-cleaned version of title column|
|alltext_clean|object|Concatenated values from clean_text and clean_title columns|
|title_word_count|int64|Count of words in clean_title column|
|selftext_word_count|int64|Count of words in clean_text column|

### Conclusion

In conclusion, I believe the Logistic Regression model is best suited for addressing our initial problem. The accuracy scores from this model are .99 on the training data and .94 on the testing data. While there is a slight amount of overfitting, a test data score of .94 is high enough to provide confidence that this will work well on unseen data as well. This model also provides  coefficients that allow for interpretation.

### Areas for Future Studies

If time and resources allowed, I would have liked to dig deeper into preprocessing and further tuning existing models. I believe that a few of the baseline models from section 5 could have been further improved with hyperparameter tuning. There are also features that I used for EDA that I would like to incorporate into a future model, such as the sentiment scores and word length. This project might be further improved through the use of Neural Networks as well.


### Sources
9/29 Breakfast Hour  
https://pushshift.io/api-parameters/  
https://www.reddit.com/r/legaladvice  
https://www.reddit.com/r/NoStupidQuestions/  
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html  
https://stackoverflow.com/questions/21492621/regex-to-keep-specific-characters-from-string  



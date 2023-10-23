#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


path_data = Path().resolve().parent / "testdata" / "sarcasm.json"
df = pd.read_json(path_data, lines=True)
df.head()
print(df.shape)


# In[20]:


df.drop(df.index[1000:],inplace=True)
df.drop(["article_link"],axis=1,inplace=True)
df.head()
print(df.shape)


# In[21]:


plt.hist(df["is_sarcastic"])
plt.show()


# In[22]:


from sklearn.feature_extraction.text import CountVectorizer


# In[23]:


cv = CountVectorizer()
#x = np.array(data["headline"])
X = cv.fit_transform(df["headline"])
df_headline = pd.DataFrame(X.todense(),columns=cv.get_feature_names_out())
df = pd.concat([df.drop(["headline"],axis=1),df_headline],axis=1)
print(df.head())
print(df.shape)


# In[24]:


pd.isna(df)


# In[25]:


df[df.isna().any(axis=1)]


# In[26]:


df[df.isnull().any(axis=1)]


# In[27]:


dfdelete = np.array(df[df.isna().any(axis=1)].index,df[df.isnull().any(axis=1)].index)
dfdelete = np.unique(dfdelete)
df.drop(dfdelete,inplace=True)
print(df.shape)


# In[28]:


df["is_sarcastic"].head()


# In[29]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop(["is_sarcastic"],axis=1), 
                                                    df['is_sarcastic'], test_size=0.30, 
                                                    random_state=111)


# In[30]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
nsimu=200+1
penalty=[0]*nsimu
logmodel=[0]*nsimu
predictions =[0]*nsimu
class_report = [0]*nsimu
f1=[0]*nsimu


# In[31]:


print("Starting")
for i in range(1,nsimu):
    logmodel[i] =(LogisticRegression(C=i/1000,solver="liblinear"))
    #logmodel[i] =(LogisticRegression(C=i/nsimu,solver="liblinear"))
    logmodel[i].fit(X_train,y_train)
    predictions[i] = logmodel[i].predict(X_test)
    class_report[i] = classification_report(y_test,predictions[i])
    l=class_report[i].split()
    f1[i] = l[len(l)-2]
    penalty[i]=1000/i

plt.scatter(penalty[1:len(penalty)-2],f1[1:len(f1)-2])
plt.title("F1-score vs. regularization parameter",fontsize=20)
plt.xlabel("Penalty parameter",fontsize=17)
plt.ylabel("F1-score on test data",fontsize=17)
plt.show()


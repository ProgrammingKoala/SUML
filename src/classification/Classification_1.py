#!/usr/bin/env python
# coding: utf-8

# In[35]:


import time
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


path_data = Path().resolve().parent / "testdata" / "sarcasm.json"
df = pd.read_json(path_data, lines=True)
df.head()
print(df.shape)


# In[37]:


df.drop(df.index[1000:],inplace=True)
df.drop(["article_link"],axis=1,inplace=True)
df.head()
print(df.shape)


# In[38]:


plt.hist(df["is_sarcastic"])
plt.show()


# In[39]:


from sklearn.feature_extraction.text import CountVectorizer


# In[40]:


cv = CountVectorizer()
#x = np.array(data["headline"])
X = cv.fit_transform(df["headline"])
df_headline = pd.DataFrame(X.todense(),columns=cv.get_feature_names_out())
df = pd.concat([df.drop(["headline"],axis=1),df_headline],axis=1)
print(df.head())
print(df.shape)


# In[41]:


pd.isna(df)


# In[42]:


df[df.isna().any(axis=1)]


# In[43]:


df[df.isnull().any(axis=1)]


# In[44]:


dfdelete = np.array(df[df.isna().any(axis=1)].index,df[df.isnull().any(axis=1)].index)
dfdelete = np.unique(dfdelete)
df.drop(dfdelete,inplace=True)
print(df.shape)


# In[45]:


df["is_sarcastic"].head()


# In[46]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop(["is_sarcastic"],axis=1), 
                                                    df['is_sarcastic'], test_size=0.30, 
                                                    random_state=111)


# In[47]:


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
nsimu=200+1
logpenalty=[0]*nsimu
logmodel=[0]*nsimu
logpredictions =[0]*nsimu
logclass_report = [0]*nsimu
logf1=[0]*nsimu


# In[48]:


print("Starting")
for i in range(1,nsimu):
    logmodel[i] =(LogisticRegression(C=i/1000,solver="liblinear"))
    #logmodel[i] =(LogisticRegression(C=i/nsimu,solver="liblinear"))
    logmodel[i].fit(X_train,y_train)
    logpredictions[i] = logmodel[i].predict(X_test)
    logclass_report[i] = classification_report(y_test,logpredictions[i])
    l=logclass_report[i].split()
    logf1[i] = l[len(l)-2]
    logpenalty[i]=1000/i

plt.scatter(logpenalty[1:len(logpenalty)-2],logf1[1:len(logf1)-2])
plt.title("Logistic Regression: F1-score vs. regularization parameter",fontsize=20)
plt.xlabel("Penalty parameter",fontsize=17)
plt.ylabel("F1-score on test data",fontsize=17)
plt.show()


# In[52]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
nsimu=200+1
maxdepth=[0]*nsimu
dectree=[0]*nsimu
decpredictions =[0]*nsimu
decclass_report = [0]*nsimu
decf1=[0]*nsimu


# In[ ]:


print("Starting")
for i in range(1,nsimu):
    dectree[i] =DecisionTreeClassifier(max_depth=pow(i,2))
    dectree[i].fit(X_train,y_train)
    decpredictions[i] = dectree[i].predict(X_test)
    decclass_report[i] = classification_report(y_test,decpredictions[i])
    l=decclass_report[i].split()
    decf1[i] = l[len(l)-2]
    maxdepth[i]=pow(i,2)

plt.scatter(maxdepth[1:len(maxdepth)-2],decf1[1:len(decf1)-2])
plt.title("Decision Tree: F1-score vs. regularization parameter",fontsize=20)
plt.xlabel("Max-depth parameter",fontsize=17)
plt.ylabel("F1-score on test data",fontsize=17)
plt.show()


# In[ ]:





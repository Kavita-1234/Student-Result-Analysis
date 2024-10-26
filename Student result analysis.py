#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install numpy
#pip install pandas
#pip install matplotlib
#pip install seaborn


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# # Drop unnamed coloumn

# In[13]:


df = df.drop("Unnamed: 0",axis = 1)
print(df.head())


# # Change weekly study hours column

# In[14]:


df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("< 5", "0 - 5")
df.head()


# # Gender distribution

# In[49]:


plt.figure(figsize=(5,5))
ax = sns.countplot(data = df, x = "Gender")
plt.title("Gender distribution")
ax.bar_label(ax.containers[0])
plt.show()


# In[ ]:


#From the above chart we have analysed that:
#the number of the females in the data is more than the number of males


# In[51]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(gb)


# In[52]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot=gb)
plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# In[ ]:


#From the above chart we have concluded that the education of the parents have a good impact on their students score


# In[47]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean', "ReadingScore":'mean', "WritingScore":'mean'})
print(gb1)


# In[53]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=gb1)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# In[ ]:


#From the above chart we have concluded that there is no/negligible on the 
#student's due to dear parents, marital status


# In[6]:


sns.boxplot(data=df, x="MathScore")
plt.show()


# In[7]:


sns.boxplot(data=df, x="ReadingScore")
plt.show()


# In[9]:


sns.boxplot(data=df, x="WritingScore")
plt.show()


# In[10]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Group

# In[21]:


groupA=df.loc[(df["EthnicGroup"] == "group A")].count()
groupB=df.loc[(df["EthnicGroup"] == "group B")].count()
groupC=df.loc[(df["EthnicGroup"] == "group C")].count()
groupD=df.loc[(df["EthnicGroup"] == "group D")].count()
groupE=df.loc[(df["EthnicGroup"] == "group E")].count()

mylist = [groupA["EthnicGroup"], groupB["EthnicGroup"], groupC["EthnicGroup"], groupD["EthnicGroup"], groupE["EthnicGroup"]]

l = ["group A", "group B", "group C", "group D", "group E"]
plt.pie(mylist, labels = l, autopct="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()


#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from statistics import mean
df = pd.read_csv("nutrition.csv")[["name","calories"]]
df.name=df.name.apply(lambda x: str(x).lower())
class Calories:
    data = df
    def get_calories(list_of_foods):
        final={}
        for foodtype in list_of_foods:
            dict_calory=[]
            for i in range(len(df.name)):
                if foodtype in df.name[i]:
                    dict_calory.append(df.calories[i])
            try:
                final[foodtype]=mean(dict_calory)
            except:
                final[foodtype]="no data"
        return final


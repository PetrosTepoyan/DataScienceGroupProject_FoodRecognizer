#!/usr/bin/env python
# coding: utf-8

# In[46]:


# !pip install clarifai


# In[63]:


from clarifai.rest import ClarifaiApp

class FoodDetector:
    
    def __init__(self, filename):
        self.filename = filename
        self.app = ClarifaiApp(api_key='4c7517bd377b4a418fffb9704d042e69')
        self.model = self.app.public_models.general_model
        self.response = self.model.predict_by_filename(filename)
        
    def get_components_with_prob(self):
        data = self.response
        dc = {}
        exclude_words = ['dinner', 'meal', 'vegetable', 'food'] # check if food
        for i in data["outputs"][0]["data"]["concepts"]: 
            name = i["name"]
            prob = i['value']
            if name not in exclude_words:
                dc[name] = prob
        
        return dc


# In[60]:





# In[35]:


# response["outputs"][0]["data"]["concepts"]


# In[33]:


# dc = {}
# exclude_words = ['dinner', 'meal', 'vegetable', 'food'] # check if food
# for i in response["outputs"][0]["data"]["concepts"]: 
#     name = i["name"]
#     prob = i['value']
# #     if name not in foods:
#     dc[name] = prob
# dc


# In[ ]:


# inter=[]
# for i in response["outputs"][0]["data"]["concepts"]:
#     if isinstance(i["name"],str ): 
#         j=i["name"]
#     if isinstance(j,str):
#         for k in a:
#             if j in k and j!="vegetable" and j!="salad" and j!="dish":
#                 inter.append(j)
# inter=set(inter)
# inter


# In[28]:


# import numpy as np
# import pandas as pd

# import requests
# from bs4 import BeautifulSoup

# from pprint import pprint
# import time
# foods=[]
# def scraper(url):
#     response=requests.get(url)
#     page=response.content
#     page=BeautifulSoup(page,'html.parser') # change type
#     return page
# for i in range(1,33):
#     url="https://foodb.ca/foods?page="+str(i)
#     page=scraper(url)
#     table=page.find("table",class_="table-foods table-standard table-condensed")
#     b=table.find_all("a",class_=None)
#     food=[i.get_text() for i in b]
#     foods+=food
# a = foods
# foods = [i.lower() for i in foods]


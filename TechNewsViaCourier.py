# Databricks notebook source
# MAGIC %md
# MAGIC **RUN CONFIGS NOTEBOOK**

# COMMAND ----------

# MAGIC %run ./configs

# COMMAND ----------

# MAGIC %md
# MAGIC **INSTALL NECESSARY PACKAGES**

# COMMAND ----------

#installing necessary packages
# !pip install bs4
# !pip install trycourier
# !pip install sumy

# COMMAND ----------

# MAGIC %md
# MAGIC **IMPORTING THE PACKAGES**

# COMMAND ----------

import requests
from bs4 import BeautifulSoup #data scraping
import json
from datetime import date

# COMMAND ----------

from sumy.summarizers.lsa import LsaSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
import nltk

# COMMAND ----------

today_date = str(date.today())
today_date

# COMMAND ----------

api_link = api_link

# COMMAND ----------

# MAGIC %md
# MAGIC **WEB SCRAPING**
# MAGIC
# MAGIC Web scraping refers to the extraction of data from a website

# COMMAND ----------

def ScrapeCode(api_link):
    req_api_link = requests.get(api_link) 

    complete_web_data = req_api_link.text
    #print(complete_web_data)

    soup_data = BeautifulSoup(complete_web_data, 'html.parser')
    #print(soup_data.prettify())

    a_class = soup_data.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"}) #data scraping

    link_list = []

    for a in a_class:
        data = a.get_text()
        news_link = a.get('href')
        if news_link.startswith("http"):
          news_link = news_link
        else:
          news_link = api_link.replace("/news/technology", "") + news_link

        news_info = data + "        " + news_link
    #     news_info = lsa_method(news_info)
        link_list.append(news_info)
      
    link_list = [*set(link_list)]
    # link_list.sort(key=len, reverse=True)
    latest_news = ""

    for i in link_list:
      latest_news += i + '\n\n'

    latest_news = "------------------------------------------TECH NEWS------------------------------------------"+"\n\n" + latest_news + "\n\n*Note: This is an auto-generated mail"

    return latest_news

# COMMAND ----------

latest_news_info = ScrapeCode(api_link)

# COMMAND ----------

# MAGIC %md
# MAGIC **NATURAL PROCESSING LANGUAGE**
# MAGIC
# MAGIC Latent Semantic Analyzer (LSA) is based on decomposing the data into low dimensional space. LSA has the ability to store the semantic of given text while summarizing.

# COMMAND ----------

def lsa_method(text):
  nltk.download('punkt')
  parser = PlaintextParser.from_string(text, Tokenizer("english"))
  summarizer_lsa = LsaSummarizer()
  summary_2 = summarizer_lsa(parser.document, 2)
  dp = []
  for i in summary_2:
    lp = str(i)
  dp.append(lp)
  final_sentence = ' '.join(dp)
  return final_sentence

# COMMAND ----------

# MAGIC %md
# MAGIC **COURIER API** 
# MAGIC
# MAGIC Courier is an API and web studio for development teams to manage all product-triggered communications (email, chat, in-app, SMS, push, etc.) in one place.

# COMMAND ----------

def SendMAILviaCourier(latest_news_info, today_date, auth_token, email_address):    
    from trycourier import Courier

    client = Courier(auth_token=auth_token)

    resp = client.send_message(
      message={
        "to": {
          "email": email_address
        },
        "content": {
          "title": "Breaking Headlines: Stay Informed with the Latest News {{date}}",
          "body": "{{info}}"
        },
        "data":{
          "info": latest_news_info,
          "date": today_date
        }
      }
    )

# COMMAND ----------

callCourierAPI = SendMAILviaCourier(latest_news_info, today_date, auth_token, email_address)

# COMMAND ----------



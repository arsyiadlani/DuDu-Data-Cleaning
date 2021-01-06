#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile


# In[67]:


# Put the location path of the input csv file here
# My Input Local Path => C:\Users\dell\Documents\DuDu\DuDu - Pembawa Pesan Sejuta Harapan(1-4)

datapath = input("Input csv datapath (Without .csv extension): ")


# In[68]:


df = pd.read_csv(datapath + ".csv")


# In[69]:


df = df.drop(["Email", "Name", 'Mau nitip pesan buat siapa dulu nih??', 'Mau nitip pesan buat Rizky juga nggak?',
              'Mau nitip pesan buat Moses juga nggak?', 'Mau nitip pesan buat siapa dulu nih??2',
              'Mau nitip pesan buat Dicky juga nggak?', 'Mau nitip pesan buat Mikha juga nggak?'], axis=1)


# In[70]:


df["Pengirim"] = df['Nama kamu siapa nih?? (Tulis nama sm angkatannya yak, contoh: SesMo - Pravala)'].fillna("Anonymous")


# In[71]:


df = df.drop(['Boleh minta nama kamu nggak nih??',
       'Nama kamu siapa nih?? (Tulis nama sm angkatannya yak, contoh: SesMo - Pravala)'], axis=1)


# In[72]:


df['Pesan untuk Moses'] = df['Mau ngasih sepatah kata apa nih buat Moses?'].combine_first(df['Mau ngasih sepatah kata apa nih buat Moses?2'])
df['Pesan untuk Rizky'] = df['Mau ngasih sepatah kata apa nih buat Rizky?'].combine_first(df['Mau ngasih sepatah kata apa nih buat Rizky?2'])
df['Pesan untuk Mikha'] = df['Mau ngasih sepatah kata apa nih buat Mikha?'].combine_first(df['Mau ngasih sepatah kata apa nih buat Mikha?2'])
df['Pesan untuk Dicky'] = df['Mau ngasih sepatah kata apa nih buat Dicky?'].combine_first(df['Mau ngasih sepatah kata apa nih buat Dicky?2'])
df['Pesan untuk Eron'] = df['Mau ngasih sepatah kata apa nih buat Eron?']


# In[73]:


df = df.drop(['Mau ngasih sepatah kata apa nih buat Moses?',
       'Mau ngasih sepatah kata apa nih buat Rizky?',
       'Mau ngasih sepatah kata apa nih buat Rizky?2',
       'Mau ngasih sepatah kata apa nih buat Moses?2',
       'Mau ngasih sepatah kata apa nih buat Mikha?',
       'Mau ngasih sepatah kata apa nih buat Dicky?',
       'Mau ngasih sepatah kata apa nih buat Dicky?2',
       'Mau ngasih sepatah kata apa nih buat Mikha?2',
       'Mau ngasih sepatah kata apa nih buat Eron?'], axis=1)


# In[74]:


df_cleaned = df[["ID", "Completion time", "Pengirim", "Pesan untuk Moses", "Pesan untuk Rizky", 
          "Pesan untuk Mikha", "Pesan untuk Dicky", "Pesan untuk Eron"]]


# In[75]:


df_cleaned = df_cleaned.rename(columns={'ID': 'No', 'Completion time': 'Waktu Pengiriman'})


# In[78]:


# Put the desired location path of the new cleaned data here
# My Output Local Path => C:\Users\dell\Documents\DuDu

output_path = input("Desired output path of the new cleaned data: ")


# In[79]:


df_cleaned.to_csv(output_path + "/DuDu_cleaned.csv", index=False)


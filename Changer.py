#!/usr/bin/env python
# coding: utf-8

# In[95]:

import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try:
    import pandas as pd
    import numpy as np
    import xlrd

except:
    install('pandas')
    install('numpy')
    install('xlrd')



import pandas as pd
import numpy as np
import os
import re


# In[96]:


if not os.path.exists("Changing"):
    os.mkdir("Changing") 


# In[97]:


Changes_File_Name = str(input("Please give the name of the file with changes.\n"))
Changes_df = pd.read_excel(Changes_File_Name)


# In[98]:


#Changes_df


# In[99]:


#for index, row in Changes_df.iterrows():
#    Changes_df.loc[index,"Condition"]


# In[100]:


Source_File_Name = str(input("Please give the name of the file where you want to bring changes.\n"))
Source_df = pd.read_excel(Source_File_Name)


# In[101]:


for index, row in Changes_df.iterrows():
    print(Changes_df.loc[index,"Condition"])
    Source_df.loc[Source_df.query(Changes_df.loc[index,"Condition"]).index, Changes_df.loc[index,"Column"]] = Changes_df.loc[index,"Value"]


# In[102]:


#Source_df


# In[103]:


from datetime import datetime
timestamp= datetime.now().strftime("%Y%m%d-%H%M%S")
Source_df.to_excel("Changing\\Changed_"+timestamp +"_"+Source_File_Name)


#!/usr/bin/env python
# coding: utf-8

# # Mining waste database
# 
# Explore the mining waste database accross Canada built from Google Earth satellite imagery. The mining sites have been identified from the **Global Tailings Portal** and several other sources including **Canadian National Pollutant Release Inventory (NPRI)**, **United States Geological Survey (USGS)** and **International Commission on Large Dams (ICOLD)** databases.

# ```{admonition} Download
# Feel free to **explore** and **download** the database .csv file [in the github](link to github) after citing us! 
# ```

# ## Quick look at the database
# 
# The **mining waste database** references the mining waste disposal sites. Each site is identified by an unique **id**. The latitude and longitude columns could help to locate the site (expressed in decimal degrees). The surface of **tailing storage facilities** (TSF), **waste rock piles** (WRP) and **open-pits** (PIT) have been calculated in **hectares**. The **province** in which the mining site is located is also recorded.
# 
# _(AB = Alberta, BC = British Columbia, MB = Manitoba, NB = New Brunswick, NL = Newfoundland and Labrador, NS = Nova Scotia, ON = Ontario, PE = Prince Edward Island, QC = Quebec, SK = Saskatchewan)_
# 
# ```{admonition} Example !
# Here is an example for the **10 biggest mining sites in Quebec** province (in total surface). 
# ```
# 

# In[1]:


import pandas as pd
url='https://raw.githubusercontent.com/AdriDim/review2022/main/database_mining_waste_canada.csv'

df = pd.read_csv(url, skiprows=0, sep=';')


# In[2]:


df_loc = df[df['PROV'] =='QC']
df_loc.sort_values(by = ['TOT(ha)'], ascending = False).head(10)


# :::{note} 
# **Cite us**: 
# Dimech, A., Cheng, L.Z., Chouteau, M., Chambers, J.E., Uhlemann, S., & Wilkinson, P.B., Meldrum, P.I., Mary, B., Fabien-Ouellet, G., & Isabelle, A. (**2022**). A review on  applications of time-lapse electrical resistivity tomography over the last 30 years : perspectives for mining waste monitoring. 
# _submitted to Engineering Geology_.
# :::

# ## Mining sites in Canada database

# In[3]:


import pandas as pd
url='https://raw.githubusercontent.com/AdriDim/review2022/main/database_mining_waste_canada.csv'

df = pd.read_csv(url, skiprows=0, sep=';')
df = df.sort_values(['TOT(ha)'], ascending=False)

from bokeh.plotting import figure, show, output_notebook
output_notebook()
from datetime import date
from random import randint

from bokeh.io import show
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn


from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

Columns = [TableColumn(field=Ci, title=Ci) for Ci in df.columns] # bokeh columns
data_table = DataTable(columns=Columns, source=ColumnDataSource(df),height = 500, width = 500) # bokeh table


# In[4]:


show(data_table)


# ```{admonition} Important note!
# :class: tip
# Please note that quarry operations might have been included in the database since a quarry open-pit looks pretty much like a mine open-pit from satellite imagery. However, quarry operations do not cover significant surface when compared to mining operations, and the total contribution of quarries in terms of surface is expected to be negligible !
# 
# Please also note that some TSFs could have been identified as WRPs (or the contrary) !
# ```

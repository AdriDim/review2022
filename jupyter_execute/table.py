#!/usr/bin/env python
# coding: utf-8

# # Sum up table

# ```{admonition} Download
# Feel free to use and download the db csv file [in the github](link to github) after citing us! 
# ```

# In[1]:


import pandas as pd
url='https://raw.githubusercontent.com/BenjMy/Dimech_etAl_TL_ERT_db/main/csv_db.csv'
df=pd.read_csv(url,skiprows=0)


# In[2]:


from bokeh.plotting import figure, show, output_notebook
output_notebook()
from datetime import date
from random import randint

from bokeh.io import show
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn


from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

Columns = [TableColumn(field=Ci, title=Ci) for Ci in df.columns] # bokeh columns
data_table = DataTable(columns=Columns, source=ColumnDataSource(df),height = 1000, width = 4000) # bokeh table


# In[3]:


show(data_table)


# <div class="alert alert-info">
# 
# Note that other libs can be used for dynamic dataframe visualisation. See https://pbpython.com/dataframe-gui-overview.html for more. Itable is also doing great!
# </div>

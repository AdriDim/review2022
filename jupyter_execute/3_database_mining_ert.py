#!/usr/bin/env python
# coding: utf-8

# # Mining ERT database
# 
# This webpage presents the database of studies applying **Electrical Resistivity Tomography** (ERT) in the context of **mining wastes**. **Over 100 studies** using ERT, published from 1990 to 2020, have been identified for the review. Each study has been classified according to the type of application. 
# 
# This database may be of help to describe the **developments of ERT** for mining waste **valorization**, mining waste **characterization** and mining waste **stability monitoring**. You may also use it to **find relevant references** for your field of expertise !
# 
# Moreover, this review helps identifying **future promising applications of TL-ERT for long-term mining waste monitoring**.

# ```{admonition} Download
# Feel free to **explore** and **download** the database .csv file [in the github project](https://github.com/AdriDim/review2022) after citing us! 
# ```

# ## Quick look at the database
# 
# The **mining waste ERT database** references published studies from 1990 to 2020 using ERT for mining waste imaging and monitoring. Each study is identified by an unique **ID** (the name of the main author and the year of publication). Other characteristics have also been recorded in the database such as the **title** of the study, the **journal** where it has been published, the **type of application**, the **country** where the study has been carried out and others.
# 
# As described in the review, the types of applications have been classified into three broader categories : 
# - **Mining waste valorization** _(Tool for heap leaching, revalorization of mineralized wastes)_
# - **Mining waste characterization** _(Waste characterization, acid mine drainage detection)_
# - **Mining waste monitoring** _(Geochemical and geotechnical mining waste stability monitoring)_
# 
# ### Example of ERT for acid mine drainage (AMD) detection
# 
# ```{admonition} Example !
# Here is an example for studies using ERT to detect and map AMD. 
# ```

# In[1]:


import pandas as pd
url='https://raw.githubusercontent.com/AdriDim/review2022/main/data/database_ert_mining_studies.csv'
df = pd.read_csv(url, skiprows=0, sep=';')
df.columns


# In[2]:


df_loc = df[df['Type of application'] =='AMD detection']
df_loc = df_loc[['ID', 'Title', 'Journal', 'Type of application', 'Country']]
df_loc.head(20)


# :::{note} 
# **Cite us**: 
# Dimech, A., Cheng, L.Z., Chouteau, M., Chambers, J.E., Uhlemann, S., & Wilkinson, P.B., Meldrum, P.I., Mary, B., Fabien-Ouellet, G., & Isabelle, A. (**2022**). A review on  applications of time-lapse electrical resistivity tomography over the last 30 years : perspectives for mining waste monitoring. 
# _submitted to Engineering Geology_.
# :::

# ## Explore the 'ERT for mining waste' database

# In[3]:


df_loc = df.sort_values(['Year'], ascending=True)

from bokeh.plotting import figure, show, output_notebook
output_notebook()

from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn


columns = [TableColumn(field=Ci, title=Ci) for Ci in df_loc.columns]

data_table_3 = DataTable(columns=columns, 
                       source=ColumnDataSource(df_loc), 
                       height = 500,
                       width = 800,
                       autosize_mode='fit_columns')


# In[4]:


show(data_table_3)


# In[5]:


df.head(0)


# In[ ]:





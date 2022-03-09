#!/usr/bin/env python
# coding: utf-8

# # TL-ERT database
# 
# This webpage presents the **Time-Lapse Electrical Resistivity Tomography** (TL-ERT) database. **Over 650 studies** using TL-ERT, published from 1990 to 2020, have been identified for the review. Each study has been classified according to the type of application, the monitoring strategy and other relevant characteristics. 
# 
# This database may be of help to describe the **dynamics of TL-ERT** for each field of application. You may also use it to **find relevant references** for your field of expertise !

# ```{admonition} Download
# Feel free to **explore** and **download** the database .csv file [in the github project](https://github.com/AdriDim/review2022) after citing us! 
# ```

# ## Quick look at the database
# 
# The **TL-ERT database** references published studies from 1990 to 2020 using TL-ERT for subsurface monitoring. Each study is identified by an unique **ID** (the name of the main author and the year of publication). Other characteristics have also been recorded in the database such as the **title** of the study, the **journal** where it has been published, the **field of application**, the **country** where the study has been carried out and others.
# 
# As described in the review, the fields of applications have been classified into four broader categories : 
# - **Hydrogeo-thermal monitoring** _(Hydrogeological, geothermal and volcanology studies)_
# - **Environmnental monitoring** _(Contaminant, saline intrusion and mining waste monitoring)_
# - **Geotechnical monitoring** _(Insfrastructure, landslide and permafrost imaging)_
# - **Ecological monitoring** _(Vegetation and CO2 storage monitoring)_
# 
# ### Example of permafrost TL-ERT studies
# 
# ```{admonition} Example !
# Here is an example for 10 studies using TL-ERT in the context of permafrost monitoring. 
# ```

# In[1]:


import pandas as pd
url='https://raw.githubusercontent.com/AdriDim/review2022/main/data/database_tlert_studies.csv'
df = pd.read_csv(url, skiprows=0, sep=';')


# In[2]:


df_loc = df[df['Field of application'] =='Permafrost']
df_loc = df_loc[['ID', 'Title', 'Journal', 'Field of application', 'Country']]
df_loc.sort_values(by = ['ID'], ascending = True).head(10)


# ### Example of semi-permanent TL-ERT studies
# 
# The **semi-permanent surveys** have been identified among all TL-ERT studies. As defined by Whiteley et al. (2019), semi-permanent surveys generally use dedicated resistivity meters left in the field all year to carry out autonomous measurements. This type of monitoring approach has been identified as particularly promising for long-term monitoring of mining waste in the review, which focuses on this application.
# 
# ```{admonition} Example !
# Here is an example for 5 studies using semi-permanent TL-ERT in the context of landslide monitoring. 
# The temporal parameters of the survey are presented (_duration of the survey, nb of snapshots, temporal resolution_).
# ```

# In[3]:


# Example of semi-permanent studies for landslide : Temporal resolution !
df_loc = df[df['Field of application'] =='Landslide']
df_loc = df_loc[df_loc['Type of survey'] =='Semi-permanent']


df_loc_temp = df_loc[['ID', 'Title', 'Type of survey', 'Field of application', 'Site name', 'Duration (days)', 'NB snapshots', 'Frequency (snapshot/day)']]
df_loc_temp.sort_values(by = ['ID'], ascending = True).head(5)


# Note that other characteristics are also recorded in the database for semi-permanent studies.
# 
# ```{admonition} Example !
# Here is an example for 5 studies using semi-permanent TL-ERT in the context of landslide monitoring. 
# The spatial parameters of the survey are presented (_electrode spacing, nb of electrodes, resistivity meter used_).
# ```

# In[4]:


df_loc_spat = df_loc[['ID', 'Title', 'Type of survey', 'Field of application', 'ERT layout',
                      'Surface (m)', 'Electrode spacing (m) ', 'Config Elec', 'Nb Elec', 'Resistivimeter']]
df_loc_spat.sort_values(by = ['ID'], ascending = True).head(5)


# :::{note} 
# **Cite us**: 
# Dimech, A., Cheng, L.Z., Chouteau, M., Chambers, J.E., Uhlemann, S., & Wilkinson, P.B., Meldrum, P.I., Mary, B., Fabien-Ouellet, G., & Isabelle, A. (**2022**). A review on  applications of time-lapse electrical resistivity tomography over the last 30 years : perspectives for mining waste monitoring. 
# _submitted to Engineering Geology_.
# :::
# 
# [![DOI](https://zenodo.org/badge/465892724.svg)](https://zenodo.org/badge/latestdoi/465892724)

# ### Explore TL-ERT studies on a map

# :::{figure-md} markdown-fig
# <img src='https://raw.githubusercontent.com/AdriDim/review2022/main/image/tlert_map.svg' alt="tlert_map" class="bg-primary mb-1" width="800px">
# 
# Distribution of TL-ERT studies from 1990 to 2020 on a map, 
# number of published studies for the top-10 countries.
# :::

# ## Explore the 'TL-ERT' database

# In[5]:


df_loc = df.sort_values(['Year'], ascending=True)

from bokeh.plotting import figure, show, output_notebook
output_notebook()

from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn


columns = [TableColumn(field=Ci, title=Ci) for Ci in df_loc.columns]

data_table_2 = DataTable(columns=columns, 
                       source=ColumnDataSource(df_loc), 
                       height = 500, 
                       width = 800,
                       autosize_mode='fit_columns')


# In[6]:


show(data_table_2)


# In[7]:


df.head(0)


# In[ ]:





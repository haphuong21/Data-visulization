#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Ex 1: Caculate the average station's elevation of station that dataype contain 'SNOW' and station name contains 'NJ US'
# In[5]:


nyc_weather = pd.read_csv("nyc_weather_2018.csv")
weather_station = pd.read_csv("weather_stations.csv")


# In[51]:


nyc_weather


# In[66]:


weather_station


# In[57]:


merging = nyc_weather.drop_duplicates(subset = ["datatype","station"]).merge(weather_station.rename(dict(id="station"), axis = 1), on= "station")


# In[56]:


merging[(merging.datatype == "SNOW")&(merging.name.str.contains("NJ US"))]


# In[58]:


merging[(merging.datatype == "SNOW")&        (merging.name.str.contains("NJ US"))]["elevation"].mean()


# In[67]:


nyc_weather

Ex2
# In[68]:


fb = pd.read_csv("fb_2018.csv")
fb


# In[74]:


fb2 = fb.assign(volume_pct_change = fb.volume.pct_change()).fillna(0)


# In[75]:


fb2


# In[78]:


fb2.sort_values(by = "volume_pct_change",ascending=False).head(5)


# In[79]:


fb2.nlargest(5,columns="volume_pct_change")

Ex 3:
# In[80]:


dt = pd.read_csv("earthquakes.csv")


# In[81]:


dt


# In[89]:


bins = pd.IntervalIndex.from_tuples([(0, 1), (1, 2), (4, 7)])
pd.cut(dt[dt.magType=="ml"].mag, bins, labels=["first","second","third"]).value_counts()


# In[91]:


pd.cut(dt[dt.magType=="ml"].mag, bins = 3).value_counts()

Ex 4
•Calculate the mean value each station recorded snow per month.
•Count the number of times each station recorded snow per month.
# In[14]:


data = pd.read_csv("weather_by_station.csv",index_col="date",parse_dates=True)
snow_data = data.query("datatype == 'SNOW'")
snow_data


# In[17]:


snow_data.groupby(["station",snow_data.index.month]).agg({"value":"mean"})


# In[13]:


pd.crosstab(index = snow_data.station_name, columns = snow_data.index.month,           colnames=["month"],values = snow_data.value,aggfunc=lambda x:(x>0).sum(),           margins=True, margins_name="total observations of snow")


# In[ ]:





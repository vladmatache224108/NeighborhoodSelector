import streamlit as st  # Importing the Streamlit library
import pandas as pd  # Importing pandas for data manipulation
import geopandas as gpd  # Importing geopandas for working with geographic data
import numpy as np  # Importing numpy for numerical computations
import altair as alt  # Importing altair for data visualization
from streamlit_extras.app_logo import add_logo  # Importing the add_logo function from streamlit_extras.app_logo module

add_logo("streamlit/logo.png", height=180)  # Adding a logo to the Streamlit app

# Reading the content of markdown files into variables
with open('streamlit\scripts\VladReport.md') as f:
    vlad_report = f.read()

with open('streamlit\scripts\PannaReport.md') as f:
    panna_report = f.read()

with open('streamlit\scripts\EDA_Report.md') as f:
    eda_report = f.read()

# Function for plotting below the tabs
def plot_below():
        df = 'C:/Users/bogda/Documents/GitHub/2022-23d-1fcmgt-reg-ai-01-group-team9/Code & Data/data_merged/full_join.geojson'

        df = gpd.read_file(df)


        df = df.drop(['geometry','price_2015', 'price_2016', 'price_2017',
                'price_2018', 'price_2019', 'price_2020', 'price_2021',
                'Encroachment on public order', 'Fraud (other)', 'Horizontal Fraud',
                'Human trafficking', 'Nature and landscape', 'Quality of life (other)',
                'Road (other)', 'Spatial planning', 'Special Laws',
                'Transport of hazardous substances', 'Under the influence (water)',
                'Air (other)', 'Animals', 'Arms Trade', 'Building materials',
                'Cybercrime', 'Discrimination', 'Domestic Violation',
                'Fire/Explosion','Fireworks', 'Food safety', 'Home theft/burglary',
                'Immigration care','Most', 'Motor Vehicle Theft', 'Murder, Manslaughter',
                'Neighbor rumor (relationship problems)', 'Open violence (person)','Other property crimes',
                'People smuggling', 'Pesticides','Pickpocketing', 'Robbery', 'Shoplifting', 'Soil',
                'Structure of the Environmental Management Act','Theft from/from motor vehicles',
                'Theft/burglary of companies, etc.','Thefts (water)', 'Threat',  'Under the influence (air)',
                'Under the influence (road)','Vertical Fraud', 'Waste', 'Water',
                'Youth nuisance report','Nuisance drifters', 'Noise nuisance catering',
                'Noise nuisance event', 'Other noise nuisance', 'Childcare',
                'Education', 'Health and well-being', 'Hospitality', 'Retail',
                ], axis = 1)
        df_eh = df.drop(['neighborhood', 'regions'], axis = 1)
        df = df.replace(np.nan, 0)
        data = df
        for column in df_eh.columns:
                line_chart = alt.Chart(data).mark_bar().encode(
                    x=alt.X("neighborhood:N", sort = '-y'),
                    y=alt.Y("sum(" + column + '):Q'))
                tab2.altair_chart(line_chart, use_container_width=True)
                corr = "Spearman's Corr for price and " + column + ' = ' + str(data['price_2022'].corr(data[column], method='spearman'))
                tab2.subheader(corr)
                tab2.markdown('\n')
                tab2.markdown('\n')
                tab2.markdown('\n')
                tab2.markdown('\n')
                tab2.markdown('\n')
                tab2.markdown('\n')




# Setting the title and subtitle of the Streamlit app
title = st.title('Data Analysis')
subtitle = st.subheader('-Team GeoNinjas')

# Creating three tabs with labels
tab1, tab2, tab3 = st.tabs(["Green Index", 'Crime & Nuisance', 'EDA Report'])

# Displaying the content of markdown reports in each tab
tab1.markdown(vlad_report)
tab2.markdown(panna_report)
tab3.markdown(eda_report)



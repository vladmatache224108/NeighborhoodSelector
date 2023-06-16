import streamlit as st  # Importing the Streamlit library
import pandas as pd  # Importing the Pandas library

# Importing the `add_logo` function from the `app_logo` module of `streamlit_extras` package
from streamlit_extras.app_logo import add_logo

# Adding a logo to the Streamlit app
add_logo("streamlit/logo.png", height=180)

# Creating a title for the app
title = st.title('Data Analysis')

# Creating a caption for the app
caption = st.caption('-Team GeoNinjas| Panna Pfandler in collaboration with the others')

# Reading the content of the file 'DEDA.md' and assigning it to the variable 'deda'
with open('streamlit/scripts/ethics/DEDA.md') as f:
    deda = f.read()

# Rendering the content of 'DEDA.md' as Markdown using the `markdown` function of Streamlit
st.markdown(deda)

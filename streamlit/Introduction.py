import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

add_logo("streamlit/logo.png", height=180)




title = st.title('Neighbourhood Index')
caption = st.caption('-Team GeoNinjas|Panna Pfandler')


with open("streamlit\scripts\Introduction.md") as f:
    introduction = f.read()

st.markdown(introduction)
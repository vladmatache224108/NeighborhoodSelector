# Importing the required libraries
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

# Adding the logo to the Streamlit app
add_logo("streamlit/logo.png", height=180)

# Reading the content of markdown files into variables
with open('streamlit/scripts/ethics/Accountability.md') as f:
    accountability = f.read()

with open('streamlit/scripts/ethics/Human Agency and Autonomy.md') as f:
    human_agency = f.read()

with open('streamlit/scripts/ethics/Diversity, Non-discrimination.md') as f:
    diversity = f.read()

with open('streamlit/scripts/ethics/Privacy and Data Governance.md') as f:
    privacy = f.read()

with open('streamlit/scripts/ethics/Societal and Environmental.md') as f:
    societal = f.read()

with open('streamlit/scripts/ethics/Technical Robustness and Safety.md') as f:
    tech = f.read()

with open('streamlit/scripts/ethics/Transparency.md') as f:
    transparency = f.read()

# Setting the title and caption of the Streamlit app
title = st.title('ALTAI')
caption = st.caption('-Team GeoNinjas|Thijn Van Oort & Vlad Matache')

# Creating seven tabs with labels
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Human Agency and Autonomy", "Privacy and Data Governance",
                                                   "Accountability", "Diversity, Non-discrimination", 
                                                   "Societal and Environmental", "Technical Robustness and Safety",
                                                   "Transparency"])

# Displaying the content of markdown reports in each tab
# along with respective contributors
# GeoNinjas method applied: Adding comments to each tab
tab1.markdown(human_agency)  # Displaying content
tab1.markdown("- Panna.")  # Adding contributor comment

tab2.markdown(privacy)  # Displaying content
tab2.markdown("- Wojciech.")  # Adding contributor comment

tab3.markdown(accountability)  # Displaying content
tab3.markdown("- Vlad.")  # Adding contributor comment

tab4.markdown(diversity)  # Displaying content
tab4.markdown("- Thijn.")  # Adding contributor comment

tab5.markdown(societal)  # Displaying content
tab5.markdown("- Thijn.")  # Adding contributor comment

tab6.markdown(tech)  # Displaying content
tab6.markdown("- Thijn.")  # Adding contributor comment

tab7.markdown(transparency)  # Displaying content
tab7.markdown("- Thijn.")  # Adding contributor comment

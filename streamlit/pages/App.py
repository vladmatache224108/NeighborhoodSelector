# Importing necessary libraries
import streamlit as st
import pandas as pd
import altair as alt
import geopandas as gpd
import numpy as np
import time
from streamlit_extras.app_logo import add_logo
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_toggle import st_toggle_switch
from streamlit_extras.dataframe_explorer import dataframe_explorer


def style_metric_cards(
    background_color: str = "#F9ADA0",
    border_size_px: int = 1,
    border_color: str = "#2E933C",
    border_radius_px: int = 5,
    border_left_color: str = "#887CAF",
    box_shadow: bool = True,
    ):
    '''
    function that defines the style formatting for the metric cards.
    '''
    box_shadow_str = (
        "box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;"
        if box_shadow
        else "box-shadow: none !important;"
    )
    st.markdown(
        f"""
        <style>
            div[data-testid="metric-container"] {{
                background-color: {background_color};
                border: {border_size_px}px solid {border_color};
                padding: 5% 5% 5% 10%;
                border-radius: {border_radius_px}px;
                border-left: 0.5rem solid {border_left_color} !important;
                {box_shadow_str}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def get_weights(slider_scores):
    '''
    Anction thst returns all inforamtion needed to calculate scores based on the
    values provided by sliders.

    Input:
        slider_scores: a list containing all the sliders' values
    
    Output:
        dict: a dictionary with feature name, slider score, and ascending boolean combined
    '''
    features_list = ['sport_building_count',
                    'distance_from_centre_km',
                    'green_score',
                    'livability_score',
                    'jobs_count',
                    'price_2022',
                    'proximity_score',
                    'density',
                    'crime_and_nuisance']
    asc_bool_list = [False, True, False, False, False, True, False, True, True]
    return {features_list[i]: (slider_scores[i], asc_bool_list[i]) for i in range(len(features_list))}

def percentage_change(col1, col2):
    '''
    A function that returns the percentage change using two dataframe columns

    Input:
        col1: a dataframe column
        col2: a dataframe column
    
    Output:
        A number representing the percentage change
    '''
    return ((col2 - col1) / col1) * 100

def show_results(sums, scores, planning_mode, copy):
    '''
    Shows results based on the weights that user chooses using the sliders.
    '''
    if planning_mode:
        sums = sums.sort_values('total', ascending = False)
        adjective = 'Worst'
        normalizer = 1
    else:
        adjective = 'Best'
        normalizer = -1
    
    best_neighborhood = sums.iloc[0]['neighborhood']
    second_neighborhood = sums.iloc[1]['neighborhood']
    st.header('The ' + adjective + ' neighborhood for you is: ' + best_neighborhood)
    st.subheader('Analysis of ' + best_neighborhood + ' versus ' + second_neighborhood)
    best_score = scores[scores['neighborhood'] == best_neighborhood]
    second_score = scores[scores['neighborhood'] == second_neighborhood]
    comparison = pd.concat([best_score, second_score]).T.reset_index()
    comparison.columns = comparison.iloc[0]
    comparison = comparison.tail(-2).sort_values([best_neighborhood,second_neighborhood], ascending= False)
    comparison = comparison.assign(
        metrics = (normalizer * percentage_change(comparison[best_neighborhood],comparison[second_neighborhood]))
            .astype('float')
            .round(2)
        )
    comparison['metrics'] = comparison['metrics'].astype(str) + '%'
    top3_metrics = comparison.head(3)

    tab1, tab2, tab3 = st.tabs(['Cards','Charts','Raw Data'])
    with tab1:
        col1, col2, col3 = st.columns(3)

        col1.metric(label=top3_metrics['neighborhood'].iloc[0], value=top3_metrics[best_neighborhood].iloc[0], delta=top3_metrics['metrics'].iloc[0])

        col2.metric(label=top3_metrics['neighborhood'].iloc[1], value=top3_metrics[best_neighborhood].iloc[1], delta=top3_metrics['metrics'].iloc[1])
    
        col3.metric(label=top3_metrics['neighborhood'].iloc[2], value=top3_metrics[best_neighborhood].iloc[2], delta=top3_metrics['metrics'].iloc[2])
        st.caption(adjective + ' neighborhood compared to second ' + adjective + '.')
        st.caption('Score is a numerical representation of the metric.')
        style_metric_cards()
    with tab2:
        copy_2 = copy[['neighborhood', 'price_2015', 'price_2016', 'price_2017',
                    'price_2018', 'price_2019', 'price_2020', 'price_2021', 'price_2022']]
        copy_2 = pd.melt(copy, id_vars=['neighborhood'], value_vars=['price_2015', 'price_2016', 'price_2017',
                    'price_2018', 'price_2019', 'price_2020', 'price_2021', 'price_2022'])
        copy_2 = copy_2.rename(columns = {'variable':'price_year','value':'price(€)'})
        copy_2 = copy_2[copy_2['neighborhood'].isin([best_neighborhood,second_neighborhood])]
        line_chart = alt.Chart(copy_2).mark_line().encode(
                    x=alt.X("price_year:N"),
                    y=alt.Y("price(€):Q"),
                    color = 'neighborhood:N')
        tab2.altair_chart(line_chart, use_container_width=True)
    with tab3:

        st.dataframe(copy, use_container_width=True)


MIN = 1
MAX = 9

neighborhood_planner_toggle = st_toggle_switch(
    label="Neighbourhood Planner mode",
    key="switch_1",
    default_value=False,
    label_after=False,
    inactive_color="#D3D3D3",
    active_color="#11567f",
    track_color="#29B5E8",
)

add_logo('streamlit/logo.png', height=180)

title = st.title('Neighbourhood Selector')
caption = st.caption('-Team GeoNinja| Vlad Matache & Wojciech Stachowiak')
add_vertical_space(4)
st.markdown("This app's purpose is to suggest to you the best neighbourhood to move in to, based on the importance you allocate to different factors.")
st.markdown('After allocating all of your points press the "Begin!" button in order to process your data.')
st.markdown("\n")
st.subheader("You have 50 points in total to allocate.")


slider_scores = [
    st.slider('Importance of proximity to sport accomodations', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of proximity to the center of Breda', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of green spaces', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of livability score', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of availability of jobs', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of house prices', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of proximity to facilities(hospitals, supermarkets, schools, etc.)', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of population density', min_value = MIN, max_value = MAX, value = 5),
    st.slider('Importance of crime and nuisance', min_value = MIN, max_value = MAX, value = 5)
]

remaining_points = int(50 - sum(slider_scores))
st.text('Points remaining:'+ str(remaining_points))

class neighborhood_sorter():
    '''
    This is a class that stores all the code for chosing the best neighborhood
    based on weighted feature scores. The lower the score of a neighborhood,
    The better match with the user's preferences.

    Input while instantiating:
        df: a dataframe that contains all the merged data (don't touch that)
        weights: a dictionary containing all the column names,
            weights and sorting directions for each feature
    
    Output:
        df: a Pandas DataFrame containing all the neiborhoods
        sorted ascending (from best match to worst) with the scores
    '''
    def __init__(self,
                 df,
                 weights=get_weights(slider_scores)):
        
        self.df = df
        self.weights = weights
    
    def preprocess_data(self):
        '''
        A function that assigns new columns, drops unused ones and returns cleaned
        dataframe ready for assigning scores to features.

        Output:
            df: a Pandas DataFrame
        '''
        df = self.df.assign(
            density = self.df['inhabitants'] / self.df['area_sqkm'],
            crime_and_nuisance = self.df['Total felonies'] + self.df['Total nuisance registrations'])

        df = df.drop(['Accidents (road)',
            'Encroachment on public order', 'Fraud (other)', 'Horizontal Fraud',
            'Human trafficking', 'Nature and landscape', 'Quality of life (other)',
            'Road (other)', 'Spatial planning', 'Special Laws',
            'Transport of hazardous substances', 'Under the influence (water)',
            'Abuse', 'Air (other)', 'Animals', 'Arms Trade', 'Building materials',
            'Cybercrime', 'Discrimination', 'Domestic Violation',
            'Drug trafficking', 'Drugs/drink nuisance', 'Fire/Explosion',
            'Fireworks', 'Food safety', 'Home theft/burglary', 'Immigration care',
            'Most', 'Motor Vehicle Theft', 'Murder, Manslaughter',
            'Neighbor rumor (relationship problems)', 'Open violence (person)',
            'Other property crimes', 'People smuggling', 'Pesticides',
            'Pickpocketing', 'Robbery', 'Shoplifting', 'Soil', 'Street robbery',
            'Structure of the Environmental Management Act',
            'Theft from/from motor vehicles',
            'Theft of mopeds, mopeds and bicycles',
            'Theft/burglary box/garage/shed', 'Theft/burglary of companies, etc.',
            'Thefts (water)', 'Threat', 'Total felonies',
            'Under the influence (air)', 'Under the influence (road)',
            'Vertical Fraud', 'Waste', 'Water'], axis=1)
        
        df = df.drop(['Total nuisance registrations',
                    'Nuisance by confused person',
                    'Youth nuisance report',
                    'Nuisance due to alcohol/drugs',
                    'Nuisance drifters',
                    'Public intoxication',
                    'Noise nuisance catering',
                    'Noise nuisance event',
                    'Other noise nuisance'],
                    axis=1)
        
        df = df.drop(['Childcare',
                    'Education',
                    'Health and well-being',
                    'Hospitality',
                    'Retail',
                    'inhabitants',
                    'light_count',
                    'light_per_1000',
                    'workplace_count',
                    'sport_building_per_1000',
                    'area_sqkm',
                    'drug_store_count'],
                    axis=1)
        
        return df
    
    def create_scores(self, df):
        '''
        A function that assigns points for each feature based on the neiborhood's place (after sorting)
        
        Input:
            df: a Pandas DataFrame preprocessed with 'preprocess_data' function
        
        Output:
            df_scores: a Pandas DataFrame with all the points for every feature
        '''
        df_scores = df[['neighborhood']]
        for feature, (weight, asc_bool) in self.weights.items():
            df_merge = df.sort_values(feature, ascending=asc_bool, ignore_index=True)[['neighborhood']]
            df_merge = df_merge.assign(score = weight * pd.Series([x + 1 for x in range(56)]))
            df_scores = df_scores.merge(df_merge, how='left', on='neighborhood', suffixes=(None, f'_{feature}'))
        return df_scores
    
    def summarize_scores(self):
        '''
        A function that summarizes the score columns created by 'create_scores' function.

        Output:
            df: a Pandas DataFrame containing all the neighborhoods
                sorted ascending (from best match to worst) with the scores
            scores: a Pandas DataFrame with scores per feature
        '''
        df = self.preprocess_data()
        df = self.create_scores(df)
        df = df.assign(total = (
            df['score']+
            df['score_distance_from_centre_km']+
            df['score_green_score']+
            df['score_livability_score']+
            df['score_jobs_count']+
            df['score_price_2022']+
            df['score_proximity_score']+
            df['score_density']+
            df['score_crime_and_nuisance']))
        
        scores = df[['neighborhood','score','score_distance_from_centre_km','score_distance_from_centre_km', 'score_livability_score', 
                     'score_jobs_count', 'score_price_2022', 'score_proximity_score', 'score_density','score_crime_and_nuisance']]
        
        return df[['neighborhood', 'total']].sort_values('total').reset_index(drop = True), scores
    
# reading the data from a file
df = gpd.read_file('Code & Data/data_merged/full_join.geojson')
# getting rid of geometry column
df = df.drop('geometry', axis = 1)

begin_button = st.button('Begin!')

# checking if the points are correctly distributed
if begin_button:
    if remaining_points >= 0:
        with st.spinner('Neighborhood Selector is casting spells...'):
            time.sleep(2)
            sorter = neighborhood_sorter(df)
            sums, scores = sorter.summarize_scores()
            st.success('Done!')
            show_results(sums, scores, neighborhood_planner_toggle, df)

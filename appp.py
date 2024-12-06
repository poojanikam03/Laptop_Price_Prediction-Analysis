import streamlit as st
import numpy as np
import pandas as pd
import plotly_express as px

df=pd.read_csv("Cleanedlaptop.csv")

st.title("Price Analysis Dashboard")
st.markdown("Explore the variation of Price with other columns in the dataset.")

#sidebar
categorical_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
numerical_cols = ['Ram', 'Weight', 'TouchScreen', 'IPS', 'ppi']

all_cols= categorical_cols + numerical_cols
selected_column = st.sidebar.selectbox("Select a column to compare",all_cols)

#Plotting 
if selected_column:
    if selected_column in categorical_cols:
        fig=px.box(df,x=selected_column,y='Price',title=f'Price Variation by {selected_column}')
    else:
         fig=px.scatter(df,x=selected_column,y='Price',trendline="ols",title=f'Price vs {selected_column}')
        
        
st.plotly_chart(fig)
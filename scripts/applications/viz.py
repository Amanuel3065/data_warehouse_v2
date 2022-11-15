import streamlit as st
import pandas as pd
import os
import sys



def app():

    st.title("Features Analysis")

    df_cleaned = pd.read_csv('data/datamod1.csv')
    

    st.header("vehicle type")
    
    st.bar_chart(df_cleaned['type'])


import streamlit as st
import pandas as pd
import os
import sys



def app():

    st.title("Features Analysis")

    df_cleaned = pd.read_csv('data/datamod1.csv')
    

    st.header("locomotive types")
    st.subheader("most objects in an asset")
    st.line_chart(df_cleaned['type'])


    
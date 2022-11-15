import os
import sys
import streamlit as st

sys.path.insert(0, './scripts')

from multiapp import MultiApp
from applications import viz

st.set_page_config(page_title="Feature Visualization", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# features
""")

# Add all your application here
app.add_app("visualization", viz.app)


# The main app
app.run()
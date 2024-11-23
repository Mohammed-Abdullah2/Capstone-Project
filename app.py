import streamlit as st
import pandas as pd

df = pd.read_csv('youtube_data_eda.csv')

st.set_page_config(layout="wide")

st.title('DataTube')

option = st.selectbox(
    "How would you like to be contacted?",
    (df['profile_name']),
    index=None,
    placeholder="Select contact method...",
)

st.write("You selected:", option)

st.dataframe(df)

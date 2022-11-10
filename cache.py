import streamlit as st
import pandas as pd

st.title('Streamlit con cache')

data_url = 'dataset.csv'

@st.cache
def load_data(nrows): 
    data = pd.read_csv(data_url, nrows = nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state = st.text('Done! 😁')

st.dataframe(data)
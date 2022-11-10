import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit - Search Names')

dataurl = 'dataset.csv' 

@st.cache
def load_data_byname(name):
    data = pd.read_csv(dataurl)
    filtered = data[data['name'].str.contains(name)]
    return filtered

myname = st.text_input('Name: ')
if myname:
    filterednames = load_data_byname(myname)
    count_rows = filterednames.shape[0]
    st.write(f'Total names: {count_rows}')
    st.dataframe(filterednames)
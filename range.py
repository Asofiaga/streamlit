import streamlit as st
import pandas as pd

st.title('Streamlit - Searchranges')

data_url = 'dataset.csv'

@st.cache
def load_data_range(startid, endid): 
    data = pd.read_csv(data_url)
    filtered = data[(data['index']>=startid) & (data['index']<=endid)]
    return filtered

startid = st.text_input('Start index: ')
endid = st.text_input('End index: ')
bttnrange = st.button('Search by range')

if bttnrange:
    new = load_data_range(int(startid),int(endid))
    countrows = new.shape[0]
    st.write(f'Total items: {countrows}')

    st.dataframe(new)
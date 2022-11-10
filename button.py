import streamlit as st
import pandas as pd
import numpy as np

myname = st.text_input('Name: ')

if st.button('Serch'):
    st.write(f'Search name: {myname}')


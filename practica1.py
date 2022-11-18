import streamlit as st
import pandas as pd

rawdata = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data = pd.read_csv(rawdata)
st.title('Práctica 1 - Walmart USA')

col1, col2 = st.columns([3,1],gap="large")

# filtros
with col2:
    st.header('Controles')
    st.caption('''Filtros interactivos que, una vez configurados,
    permiten el dinamismo con el muestreo de la información.''')
    shipmode = st.checkbox("Aquí va el Check-box:", ':)')
    st.markdown("___")

    selected_categ = st.selectbox("Aquí va el Select-box:", 'hola')     

# sección que muestra el dataframe filtrado
with col1:
    st.subheader('Objetivo:')
    st.caption('Crear apartado para filtros no funcionales.')
    st.dataframe(data)

"Sofía Gutiérrez - A00827191"
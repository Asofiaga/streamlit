import streamlit as st
import pandas as pd

rawdata = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data = pd.read_csv(rawdata)
st.title('Práctica 2 - Walmart USA')

col1, col2 = st.columns([3,1],gap="large")

# filtros
with col2:
    st.header('Controles')
    st.caption('Filtros dinámicos e interactivos para la información.')
    shipmode = st.radio("Ship mode", data['Ship Mode'].unique())
    st.markdown("___")

    selected_categ = st.selectbox("Categoría", data['Category'].unique()) 
    st.markdown("___")
    
    desc = st.slider(
        "Rango de Descuento", min_value=float(data['Discount'].min()), max_value=float(data['Discount'].max())
    )    

# sección que muestra el dataframe filtrado
with col1:
    st.subheader('Objetivo:')
    st.caption('Crear diversos filtros funcionales para analizar ventas de Walmart USA.')
    st.dataframe(data.loc[(data['Ship Mode'] == shipmode) &
                        (data['Category'] == selected_categ) &
                        (data['Discount'] == desc)])


"Sofía Gutiérrez - A00827191"
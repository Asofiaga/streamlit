import streamlit as st
import pandas as pd

st.header('Práctica 4 - Viajes de Uber en NY')

st.subheader('Objetivo:')
st.caption('Analizar los viajes de Uber en la ciudad de Nueva York con filtros por hora.')

DATA_URL = 'uber.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data["Date/Time"] = pd.to_datetime(data["Date/Time"])
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data = load_data(1000)

hour_to_filter = st.slider(
        "Hora del día", min_value=0, max_value=23
    )

filtered_data = data[data['date/time'].dt.hour == hour_to_filter]
st.subheader(f'Mapeo de inicio de viajes a las {hour_to_filter} horas del día')

col1, col2 = st.columns(2)
with col1:
    st.dataframe(filtered_data)

with col2:
    st.map(filtered_data)

"Sofía Gutiérrez - A00827191"
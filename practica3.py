import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

rawdata = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data = pd.read_csv(rawdata)
st.title('Práctica 3 - Walmart USA')
st.subheader('Objetivo:')
st.caption('Mostrar el comportamiento de las ventas de Walmart USA a través de diversos gráficos.')

fig, ax = plt.subplots()
y_pos = data['Ship Mode']
x_pos = data['Sales']
ax.barh(y_pos, x_pos)
ax.set_xlabel("Ventas")
ax.set_ylabel("Tipo de envío")
ax.set_title('Ventas por tipo de envío')
st.header("Gráfica de Barras")
st.pyplot(fig)
st.markdown("___")

fig2, ax2 = plt.subplots()
ax2.hist(data['Segment']) 
ax2.set_title('Histograma por segmento')
st.header("Histograma") 
st.pyplot(fig2)
st.markdown("___")

group = pd.DataFrame(data.groupby(data['Category'])['Quantity'].sum())
group.reset_index(inplace=True)
fig3, ax3 = plt.subplots()
ax3.pie(group['Quantity'], labels = group['Category']) 
ax3.set_title('Cantidad vendida por categoría')
st.header("Gráfica de pastel") 
st.pyplot(fig3)

"Sofía Gutiérrez - A00827191"
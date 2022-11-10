import streamlit as st

def bienvenida(nombre):
    mymessage = 'bienvenido/a: ' + nombre
    return mymessage

myname = st.text_input('Nombre: ')
if myname:
    mensaje = bienvenida(myname)
    st.write(f' mensaje: {myname}')
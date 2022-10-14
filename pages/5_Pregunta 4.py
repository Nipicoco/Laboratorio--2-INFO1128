import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener,medfilt
import streamlit as st
st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)   
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 4')
st.image('4.png')
codigo = '''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener,medfilt

signal = np.load("signal.npy")
x = np.arange(start=0,stop=100,step=1) #definimos nuestro rango/escala
wienersignal,medsignal = wiener(signal), medfilt(signal) #usamos metodos de scipy.signal para calcular los valores del arreglo tras pasarlos por cada funcion

a=plt.figure()
a=plt.title("signal filter"),plt.xlabel('t(s)'), plt.ylabel('signal'), plt.grid() #iniciamos nuestro pyplot
a=plt.plot(x,signal), plt.plot(x,medsignal), plt.plot(x,wienersignal) #agregamos a nuestro pyplot los puntos de los arreglos signal, y los arreglos resultantes de los filtros'''
signal = np.load("signal.npy")
x = np.arange(start=0,stop=100,step=1) #definimos nuestro rango/escala
wienersignal,medsignal = wiener(signal), medfilt(signal) #usamos metodos de scipy.signal para calcular los valores del arreglo tras pasarlos por cada funcion

a=plt.figure(figsize=(12,3))
a=plt.title("signal filter"),plt.xlabel('t(s)'), plt.ylabel('signal'), plt.grid() #iniciamos nuestro pyplot
a=plt.plot(x,signal), plt.plot(x,medsignal), plt.plot(x,wienersignal) #agregamos a nuestro pyplot los puntos de los arreglos signal, y los arreglos resultantes de los filtros
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
    st.code(codigo , language='python')
st.set_option('deprecation.showPyplotGlobalUse', False)
cambio2 = ['Ocultar Gráfico','Mostrar Gráfico']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Gráfico':
    st.pyplot()

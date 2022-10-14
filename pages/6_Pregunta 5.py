import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import streamlit as st

st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)   
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 5')
st.image('5.png')
st.write('''
         t sera un arreglo de 100 puntos entre 0 y 5, este sera generado con np.linspace(), linspace es una funcion de numpy que genera un arreglo de n puntos entre dos valores.
         x = t es una asignacion de valores, x sera igual a t por lo que x sera un arreglo de 100 puntos aleatorios.
         detrender es una funcion de scipy.signal que elimina la tendencia de una señal, en este caso la señal es x.
         
         con plt.plot() se grafican las señales filtradas y no filtradas de tendencia y con plt.legend() se agrega una leyenda a la grafica.
         Seguido de esto se hara el plt para una con tendencia y otra sin tendencia.
         ''')
codigo = '''
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

t  = np.linspace(0,5,100) # 100 puntos entre 0 y 5
x  = t +np.random.normal(size=100) # 100 puntos aleatorios


#Deleting the linear trend along the data axis with the detrend function of the signal module
detrender = signal.detrend(x)


# Una tupla de la figura y la trama usando la función subplots de matplotlib y la función figure de matplotlib y figzise para definir el tamaño de la figura
#figsize en este caso es una tupla de 10, 5 que define el tamaño de la figura
plot = plt.figure(figsize=(10,3)), plt.plot(t,x,label='Tendency'), plt.plot(t,detrender,label='No Tendency'), plt.legend(), plt.grid(), plt.show()

'''

t  = np.linspace(0,5,100) # 100 puntos entre 0 y 5
x  = t +np.random.normal(size=100) # 100 puntos aleatorios


#Deleting the linear trend along the data axis with the detrend function of the signal module
detrender = signal.detrend(x)


# Una tupla de la figura y la trama usando la función subplots de matplotlib y la función figure de matplotlib y figzise para definir el tamaño de la figura
#figsize en este caso es una tupla de 10, 5 que define el tamaño de la figura
plot = plt.figure(figsize=(10,3)), plt.plot(t,x,label='Tendency'), plt.plot(t,detrender,label='No Tendency'), plt.legend(), plt.grid(), plt.show()

cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
    st.code(codigo , language='python')
st.set_option('deprecation.showPyplotGlobalUse', False)
cambio2 = ['Ocultar Gráfico','Mostrar Gráfico']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Gráfico':
    st.pyplot()
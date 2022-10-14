import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 3')
st.image('3.png')
codigo = '''import numpy as np
import matplotlib.pyplot as plt
def value(arr, range, step):
            #composito d polinomios, polyfit nos entrega los coeficientes que luego usamos para graficar
    val = np.polyval(np.polyfit(range,arr,step), range)
    return val
    #cargamos los arreglos de numpy
f1,f2 = np.load("f1.npy"),np.load("f2.npy")
x = np.arange(start=1,stop=50,step=1) #la escala que vamos a usar
val1,val2 = value(f1,x,1),value(f2,x,2) #creamos el arreglo de los coeficientes ya calculados con la funcion, x, y incremento 1
plt.figure()
plt.title("least square polynomial"),plt.xlabel('t(s)'), plt.ylabel('f(x)') #iniciamos y definimos atributos de la figura pyplot
plt.plot(x,f1,'o'), plt.plot(x,f2,'o'), plt.plot(x,val1), plt.plot(x,val2) 
#puntos de la 1        puntos de la 2       LSP de la 1     LSP de la 2
plt.grid(),plt.show()'''
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
    st.code(codigo , language='python')
def value(arr, range, step):
    val = np.polyval(np.polyfit(range,arr,step), range)
    return val
    
f1,f2 = np.load("f1.npy"),np.load("f2.npy")
x = np.arange(start=1,stop=50,step=1)
val1,val2 = value(f1,x,1),value(f2,x,2)
a = plt.figure()
a = plt.title("least square polynomial"),plt.xlabel('t(s)'), plt.ylabel('f(x)')
a = plt.plot(x,f1,'o'), plt.plot(x,f2,'o'), plt.plot(x,val1), plt.plot(x,val2)
#puntos de la 1        puntos de la 2       LSP de la 1     LSP de la 2
a = plt.grid(),plt.savefig('plot3.png')
st.set_option('deprecation.showPyplotGlobalUse', False)
cambio2 = ['Ocultar Gráfico','Mostrar Gráfico']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Gráfico':
    st.pyplot()


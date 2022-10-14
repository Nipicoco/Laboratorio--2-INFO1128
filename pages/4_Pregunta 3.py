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
st.write('''
         
Primero definimos una funcion que nos permitira graficar los valores de un arreglo, en este caso el arreglo de la imagen, con un polinomio de grado 3, y luego lo graficamos.
Tambien definimos un arreglo de 100 valores, que nos servira para graficar el polinomio, luego los graficamos usando la funcion plt.plot() de matplotlib junto con la funcion plt.show() para mostrar el grafico.

def value() es una funcion que recibe 3 parametros, el primero es el arreglo que queremos graficar, el segundo es el rango de valores que queremos graficar, y el tercero es el grado del polinomio que queremos graficar.
np.arange es una funcion que nos permite crear un arreglo de valores.

la variable val es un arreglo que contiene los valores del polinomio de grado 3, que se grafica en el rango de valores que le pasamos como parametro.

         ''')	
codigo = '''
import numpy as np
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
    val = np.polyval(np.polyfit(range,arr,step), range) #composito d polinomios, polyfit nos entrega los coeficientes que luego usamos para graficar
    return val
    
f1,f2 = np.load("f1.npy"),np.load("f2.npy")
x = np.arange(start=1,stop=50,step=1)
val1,val2 = value(f1,x,1),value(f2,x,2)
a = plt.figure(figsize=(12,3))
a = plt.title("least square polynomial"),plt.xlabel('t(s)'), plt.ylabel('f(x)')
a = plt.plot(x,f1,'o'), plt.plot(x,f2,'o'), plt.plot(x,val1), plt.plot(x,val2)
#puntos de la 1        puntos de la 2       LSP de la 1     LSP de la 2
a = plt.grid(),plt.savefig('plot3.png')
st.set_option('deprecation.showPyplotGlobalUse', False)
cambio2 = ['Ocultar Gráfico','Mostrar Gráfico']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Gráfico':
    st.pyplot()


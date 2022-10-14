import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import chebyshev,Chebyshev
from scipy import linalg

st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)   
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 6')
st.image('6.png')
st.set_option('deprecation.showPyplotGlobalUse', False)
codigo= '''
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import chebyshev,Chebyshev
from scipy import linalg

cheby = np.load("cheby.npy")#cargamos el array
rnds = np.linspace(cheby[0].min(), cheby[0].max(), 100)#generamos nums rand. en los intervalos del min y max del primer arreglo
vand = chebyshev.chebvander(cheby[0],len(cheby[0])-1)#encontramos la matriz vandermonde del grado 9
c = linalg.solve(vand,cheby[1])# type: ignore #funcion lineal para la matriz vandermonde y la segunda matriz en cheby
func = Chebyshev(c) #llama la clase para poder retornar los coeficientes de chebyshev en orden de grado inc.
figura=plt.figure() #creamos la figura
grid = plt.grid()  #creamos la figura y la grilla
title = plt.title("interpolacion de chebyshev") #creamos el titulo
xlabel=plt.xlabel("t(s)") #creamos el titulo del eje x
ylabel=plt.ylabel("f(x)")   #creamos el titulo del eje y
interpolCheb=plt.plot(rnds,func(rnds),'-b', label="interpolacion de chebyshav") #graficamos la funcion interpolada
dataPuntos=plt.plot(cheby[0],cheby[1],'o',label='data points')  #graficamos los puntos 
legend=plt.legend() # creamos la leyenda
show=plt.show() #mostramos la figura
#creamos la figura pyplot

'''	
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
    st.code(codigo , language='python')
cheby = np.load("cheby.npy")#cargamos el array
rnds = np.linspace(cheby[0].min(), cheby[0].max(), 100)#generamos nums rand. en los intervalos del min y max del primer arreglo
vand = chebyshev.chebvander(cheby[0],len(cheby[0])-1)#encontramos la matriz vandermonde del grado 9
c = linalg.solve(vand,cheby[1])# type: ignore #funcion lineal para la matriz vandermonde y la segunda matriz en cheby
func = Chebyshev(c) #llama la clase para poder retornar los coeficientes de chebyshev en orden de grado inc.
figura=plt.figure() #creamos la figura
grid = plt.grid()  #creamos la figura y la grilla
title = plt.title("interpolacion de chebyshev") #creamos el titulo
xlabel=plt.xlabel("t(s)") #creamos el titulo del eje x
ylabel=plt.ylabel("f(x)")   #creamos el titulo del eje y
interpolCheb=plt.plot(rnds,func(rnds),'-b', label="interpolacion de chebyshav") #graficamos la funcion interpolada
dataPuntos=plt.plot(cheby[0],cheby[1],'o',label='data points')  #graficamos los puntos 
legend=plt.legend() # creamos la leyenda
show=plt.show() #mostramos la figura
#creamos la figura pyplot
cambio2 = ['Ocultar Interpolacion','Mostrar Interpolacion']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Interpolacion':
    st.pyplot(show)


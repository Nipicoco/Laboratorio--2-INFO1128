import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import chebyshev,Chebyshev
from numpy import polynomial as poly
from scipy import linalg

st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)   
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 6')
st.image('6.png')
st.write('''
         Para ser capaz de resolver este ejercicio, debemos recordar que la interpolacion de Chebyshev es una interpolacion polinomial que se realiza en el intervalo [-1,1].
         Esta interpolacion se realiza de la siguiente manera:
         Se escogen los puntos de interpolacion en el intervalo [-1,1] de la siguiente manera:
         primero se escoge el punto x_0 = -1, luego se escoge el punto de interpolacion.
         luego se escoge el punto x_n = 1.
         y finalmente se realiza la interpolacion polinomial
         Chebyshev es una clase de numpy.polynomial.chebyshev, esta clase tiene metodos para realizar la interpolacion de Chebyshev, la cual realiza la interpolacion, la cual consiste en encontrar los coeficientes del polinomio interpolante. 
         ''')
st.set_option('deprecation.showPyplotGlobalUse', False)
codigo= '''
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import chebyshev,Chebyshev
from scipy import linalg

cheby = np.load("cheby.npy")#cargamos el array
rnds = np.linspace(cheby[0].min(), cheby[0].max(), 100)# primero generamos nums rand. en los intervalos del min y max del primer arreglo, luego aplicamos la funcion linspace para generar 100 numeros entre el min y max del primer arreglo
vand = chebyshev.chebvander(cheby[0],len(cheby[0])-1)#encontramos la matriz vandermonde del grado 9 y aplicamos la funcion chebvander para encontrar la matriz vandermonde de chebyshev
coeficients = linalg.solve(vand,cheby[1])# type: ignore #funcion lineal para la matriz vandermonde y la segunda matriz en cheby que nos retorna los coeficientes de chebyshev en orden de grado.
func = Chebyshev(coeficients) #llama la clase para poder retornar los coeficientes de chebyshev en orden de grado.
polinoms = poly.Chebyshev(coeficients) #llama la clase para poder retornar los polinomios de chebyshev en orden de grado.
figura=plt.figure(figsize=(15,4)) #creamos la figura
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
rnds = np.linspace(cheby[0].min(), cheby[0].max(), 100)# primero generamos nums rand. en los intervalos del min y max del primer arreglo, luego aplicamos la funcion linspace para generar 100 numeros entre el min y max del primer arreglo
vand = chebyshev.chebvander(cheby[0],len(cheby[0])-1)#encontramos la matriz vandermonde del grado 9 y aplicamos la funcion chebvander para encontrar la matriz vandermonde de chebyshev
coeficients = linalg.solve(vand,cheby[1])# type: ignore #funcion lineal para la matriz vandermonde y la segunda matriz en cheby que nos retorna los coeficientes de chebyshev en orden de grado.
func = Chebyshev(coeficients) #llama la clase para poder retornar los coeficientes de chebyshev en orden de grado.
polinoms = poly.Chebyshev(coeficients) #llama la clase para poder retornar los polinomios de chebyshev en orden de grado.
figura=plt.figure(figsize=(15,4)) #creamos la figura
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
    st.write(coeficients, polinoms)
cambio3 = ['Ocultar Conclusion','Mostrar Conclusion']
mostrar3 = st.selectbox('Seleccionar opcion',cambio3)   
if mostrar3 == 'Mostrar Conclusion':
    st.write('''
             Como podemos observar en la interpolacion de chebyshev, se puede observar que la interpolacion es mas precisa que la interpolacion de lagrange, esto se debe a que la interpolacion de chebyshev se realiza en el intervalo [-1,1] y la interpolacion de lagrange se realiza en el intervalo [0,1], tambien podemos recalcar que la interpolacion de chebyshev es mas precisa que la interpolacion de newton, esto se debe a que la interpolacion de chebyshev se realiza en el intervalo [-1,1] y la interpolacion de newton se realiza en el intervalo [0,1], por lo tanto, la interpolacion de chebyshev es la mas precisa de las interpolaciones.
             ''')


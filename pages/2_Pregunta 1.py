
import streamlit as st
import cv2
import pandas
import numpy as np
st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 1')
st.image('1.png')
st.write('''
         En este codigo se muestra como cargar una imagen y mostrarla en la GUI, partiremos usando la libreria OpenCV para cargar la imagen y luego la transformaremos
         a un formato de escala de grises.
         Tambien usaremos panda para crear una tabla con los valores de la imagen y la mostraremos en la GUI.
         En conjunto con panda y OpenCV, usaremos la libreria numpy para crear un arreglo de la imagen y luego guardaremos los datos de este arreglo dentro de una variable para poder
         tener un registro de los datos de la imagen, en este caso, los parametros de recorte de la imagen y los valores de los pixeles de la imagen.
         
         Para calcular los momentos de la imagen, usaremos la libreria OpenCV y la funcion cv2.HuMoments() para calcular los momentos Hu de la imagen y luego le aplicaremos nuevamente Moments
         Esto para poder calcular los momentos centrales de la imagen.
         
         Usaremos abs y log10 para calcular los momentos invariantes de la imagen y luego los convertiremos a valor absoluto y a escala logaritmica para hacer los numeros mas legibles.
         Por ultimo usaremos la libreria pandas para crear una tabla con los momentos invariantes de la imagen y la mostraremos en la GUI.
         ''')
codigo= '''
import cv2
import pandas
import numpy as np
image = cv2.imread("vocales.png") # Cargamos la imagen
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convertimos a escala de grises

_, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
print(image)# Binarizamos la imagen
a = image[0:100, 0:110] # Extraemos la imagen de la vocal a y e usando slicing
e = image[0:100, 120:235] # Extraemos la imagen de la vocal a y e 
i = image[0:100, 240:310]
o = image[0:100, 310:425] 
u = image[0:100, 430:540] 

# Cálculo de los momentos Hu de la imagen. Usando flatten para convertir la matriz en un vector

momentosa = (cv2.moments(a))
HuA = cv2.HuMoments(momentosa).flatten()
HuA= np.log10(abs(HuA)) # se usa log10 para obtener los momentos de Hu y abs para obtener el valor absoluto
momentose = (cv2.moments(e))
HuE = cv2.HuMoments(momentose).flatten()
HuE= np.log10(abs(HuE))# se repite el proceso para cada vocal
momentosi = (cv2.moments(i))
HuI= cv2.HuMoments(momentosi).flatten()
HuI= np.log10(abs(HuI))
momentoso = (cv2.moments(o))
HuO = cv2.HuMoments(momentoso).flatten()
HuO = np.log10(abs(HuO))
momentosu = (cv2.moments(u))    
HuU = cv2.HuMoments(momentosu).flatten()
HuU = np.log10(abs(HuU))

# Creando un dataframe con los momentos Hu de cada vocal.
df = pandas.DataFrame({"   A    ": HuA, "  E    ": HuE, "  I    ": HuI, "  O    ": HuO, "  U    ": HuU})
df.index = ['Log(H1)', 'Log(H2)', 'Log(H3)', 'Log(H4)', 'Log(H5)', 'Log(H6)', 'Log(H7)']  # type: ignore se agrega el tipo ignore para que no marque error en el index
print("Estos son los momentos de Hu de las vocales:", df)'''
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código': # Si se selecciona mostrar código se muestra el código
    st.code(codigo , language='python')
image = cv2.imread("vocales.png") # Cargamos la imagen
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convertimos a escala de grises




_, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
print(image)# Binarizamos la imagen
a = image[0:100, 0:110] # Extraemos la imagen de la vocal a y e usando slicing
e = image[0:100, 120:235] # Extraemos la imagen de la vocal a y e 
i = image[0:100, 240:310]
o = image[0:100, 310:425] 
u = image[0:100, 430:540] 

# Cálculo de los momentos Hu de la imagen. Usando flatten para convertir la matriz en un vector

momentosa = (cv2.moments(a))
HuA = cv2.HuMoments(momentosa).flatten() #se usa flatten para convertir la matriz en un vector
HuA= np.log10(abs(HuA)) # se usa log10 para obtener los momentos de Hu y abs para obtener el valor absoluto
momentose = (cv2.moments(e)) # se repite el proceso para cada vocal
HuE = cv2.HuMoments(momentose).flatten() 
HuE= np.log10(abs(HuE))
momentosi = (cv2.moments(i))
HuI= cv2.HuMoments(momentosi).flatten()
HuI= np.log10(abs(HuI))
momentoso = (cv2.moments(o))
HuO = cv2.HuMoments(momentoso).flatten()
HuO = np.log10(abs(HuO))
momentosu = (cv2.moments(u))    
HuU = cv2.HuMoments(momentosu).flatten()
HuU = np.log10(abs(HuU))



df = pandas.DataFrame({"   A    ": HuA, "  E    ": HuE, "  I    ": HuI, "  O    ": HuO, "  U    ": HuU}) 
# se crea un dataframe con los momentos de Hu de cada vocal
df.index = ['Log(H1)', 'Log(H2)', 'Log(H3)', 'Log(H4)', 'Log(H5)', 'Log(H6)', 'Log(H7)']  # type: ignore se agrega el tipo ignore para que no marque error en el index
print("\nEstos son los momentos de Hu de las vocales: \n\n", df, "\n")




conclusion = '''En este ejercicio se puede observar que los momentos de Hu de las vocales son diferentes 
por lo que se puede decir que los momentos de Hu son invariantes a rotaciones, traslaciones y escalas, lo que quiere decir que Hu es un buen descriptor para reconocer objetos en imágenes 
pero no es un buen descriptor para reconocer vocales ya que las vocales son diferentes entre sí. En este caso se puede decir que los momentos de Hu no son invariantes a traslaciones, tambien se 
puede observar que los momentos de Hu no son invariantes a rotaciones ya que las vocales tienen diferentes momentos de Hu dependiendo de la rotación que se le haga a la vocal.'''
cambio3 = ['Ocultar Momentos','Mostrar Momentos']
mostrar3 = st.selectbox('Seleccionar opcion',cambio3)
if mostrar3 == 'Mostrar Momentos':
    st.write("Momentos de Hu de las vocales")
    st.write(df)

cambio2 = ['Ocultar Conclusion','Mostrar Conclusion']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Conclusion':
    st.info(conclusion)


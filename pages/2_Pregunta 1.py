
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
codigo = '''import cv2
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
HuA= np.log10(abs(HuA)) 
momentose = (cv2.moments(e))
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

# Creando un dataframe con los momentos Hu de cada vocal.
df = pandas.DataFrame({"   A    ": HuA, "  E    ": HuE, "  I    ": HuI, "  O    ": HuO, "  U    ": HuU})
df.index = ['Log(H1)', 'Log(H2)', 'Log(H3)', 'Log(H4)', 'Log(H5)', 'Log(H6)', 'Log(H7)']  # type: ignore se agrega el tipo ignore para que no marque error en el index
print("\nEstos son los momentos de Hu de las vocales:", df)'''
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
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
HuA = cv2.HuMoments(momentosa).flatten()
HuA= np.log10(abs(HuA)) 
momentose = (cv2.moments(e))
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


# Creando un dataframe con los momentos Hu de cada vocal.
df = pandas.DataFrame({"   A    ": HuA, "  E    ": HuE, "  I    ": HuI, "  O    ": HuO, "  U    ": HuU})
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


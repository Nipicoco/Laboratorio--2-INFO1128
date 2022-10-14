
import os
import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Taller 2 Interfaces Graficas",
    page_icon="💻",
)
st.title("Taller 2 Interfaces Graficas")
st.sidebar.success("Seleccionar Pregunta")
        
st.header('Ejercicio 2')
st.image('2.png')
codigo  = '''# Crops the image and saves it as "nombre_nuevo"
def recortar(img, areas_recortes, nombre_nuevo): # img es la imagen original, areas_recortes es una tupla con las coordenadas de la esquina superior izquierda y la esquina inferior derecha del recorte, nombre_nuevo es el nombre de la imagen recortada
    imagenes_recortadas = img.crop(areas_recortes).resize((116, 116)) # recorta la imagen original y la redimensiona a 116x116
    imagenes_recortadas.save(nombre_nuevo) # guarda la imagen recortada
def rotar(img, angulo, expandir, nuevos): # img es la imagen original, angulo es el angulo de rotacion, expandir es un booleano que indica si la imagen se expande o no, nuevos es el nombre de la imagen rotada
    img_rotada = img.rotate(angulo, expand=expandir) # rota la imagen original
    img_rotada.save(nuevos)    # guarda la imagen rotada
     
    
areas_recorte = [(10, 10, 210, 220), (242, 10, 484, 207), (505, 23, 723, 198), (733, 19, 980, 202)] # tupla con las coordenadas de las esquinas de los recortes
angulo = [75, 100, 45, 120] # lista con los angulos de rotacion


figurras = 'figuras.png' # nombre de la imagen original
plantillas = Image.open('plantilla.png') # abre la imagen original
img = Image.open(figurras).convert('RGBA') # abre la imagen original y la convierte a RGBA

# Iterando sobre la lista areas_recorte y guardando cada imagen recortada con un nombre diferente.
for i, areas_recortes in enumerate(areas_recorte): # i es el indice de la lista areas_recorte, areas_recortes es el elemento de la lista areas_recorte
    filename = os.path.splitext(figurras)[0] # obtiene el nombre de la imagen original sin la extension
    ext = os.path.splitext(figurras)[1] # obtiene la extension de la imagen original
    nombre_nuevo = filename + '_recortada' + str(i) + ext # crea el nombre de la imagen recortada

    recortar(img, areas_recortes, nombre_nuevo) # llama a la funcion recortar

# Rotando la imagen 
figura1 = Image.open('figuras_recortada0.png').rotate(75, expand=True)
figura2 = Image.open('figuras_recortada1.png').rotate(100, expand=True)
figura3 = Image.open('figuras_recortada2.png').rotate(45, expand=True)
figura4 = Image.open('figuras_recortada3.png').rotate(120, expand=True)

# Guardando las imagenes rotadas
figura1.save('figura1.png')
figura2.save('figura2.png')
figura3.save('figura3.png')
figura4.save('figura4.png')

# Pegando las imagenes rotadas en la plantilla
plantillas.paste(figura1, (9, 15))
plantillas.paste(figura2, (198, 17))
plantillas.paste(figura3, (378, 8))
plantillas.paste(figura4, (590, 10))

# Guardando la imagen final
plantillas.show()
plantillas.save('plantillas.png')
'''
cambio = ['Ocultar Código','Mostrar Código']
mostrar = st.selectbox('Seleccionar opcion',cambio)
if mostrar == 'Mostrar Código':
    st.code(codigo , language='python')
# Crops the image and saves it as "nombre_nuevo"
def recortar(img, areas_recortes, nombre_nuevo):
    imagenes_recortadas = img.crop(areas_recortes).resize((116, 116))
    imagenes_recortadas.save(nombre_nuevo)
def rotar(img, angulo, expandir, nuevos):
    img_rotada = img.rotate(angulo, expand=expandir)
    img_rotada.save(nuevos)    
    
    
areas_recorte = [(10, 10, 210, 220), (242, 10, 484, 207), (505, 23, 723, 198), (733, 19, 980, 202)]
angulo = [75, 100, 45, 120]
# Una lista de tuplas. Cada tupla representa las coordenadas de la esquina superior izquierda y la
# esquina inferior derecha del rectángulo que se va a recortar.

figurras = 'figuras.png'
plantillas = Image.open('plantilla.png')
img = Image.open(figurras).convert('RGBA')

# Iterando sobre la lista areas_recorte y guardando cada imagen recortada con un nombre diferente.
for i, areas_recortes in enumerate(areas_recorte):
    filename = os.path.splitext(figurras)[0]
    ext = os.path.splitext(figurras)[1]
    nombre_nuevo = filename + '_recortada' + str(i) + ext

    recortar(img, areas_recortes, nombre_nuevo)

# Rotando la imagen
figura1 = Image.open('figuras_recortada0.png').rotate(75, expand=True)
figura2 = Image.open('figuras_recortada1.png').rotate(100, expand=True)
figura3 = Image.open('figuras_recortada2.png').rotate(45, expand=True)
figura4 = Image.open('figuras_recortada3.png').rotate(120, expand=True)

# Guardando las imagenes rotadas
figura1.save('figura1.png')
figura2.save('figura2.png')
figura3.save('figura3.png')
figura4.save('figura4.png')

# Pegando las imagenes rotadas en la plantilla
plantillas.paste(figura1, (9, 15))
plantillas.paste(figura2, (198, 17))
plantillas.paste(figura3, (378, 8))
plantillas.paste(figura4, (590, 10))

# Guardando la imagen final

plantillas.save('plantillas.png')

cambio2 = ['Ocultar Imagen','Mostrar Imagen']
mostrar2 = st.selectbox('Seleccionar opcion',cambio2)
if mostrar2 == 'Mostrar Imagen':
    st.image('plantillas.png')
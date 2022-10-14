
import os

from PIL import Image

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
plantillas.show()
plantillas.save('plantillas.png')

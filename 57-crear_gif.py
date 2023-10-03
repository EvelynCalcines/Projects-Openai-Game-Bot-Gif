import imageio
import cv2  # Para redimensionar las imágenes

# Definir las rutas de las imágenes
filenames = ['equipo-pic1.jpg', 'equipo-pic2.jpg']
images = []

# Redimensionar todas las imágenes a 200x200 píxeles
desired_size = (200, 200)
for filename in filenames:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
    img = cv2.resize(img, desired_size)
    images.append(img)

# Guardar el GIF
imageio.mimsave('equipo5.gif', images, duration=2.0, palettesize=256)

# Imprimir un mensaje de confirmación
print("El GIF 'equipo5.gif' se ha creado con éxito.")

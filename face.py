import PIL.Image
import PIL.ImageDraw
import face_recognition

# Charger l'image à analyser 
image = face_recognition.load_image_file("img2.jpg")

# Trouver tous les visages dans l'image
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print("On a {} visage(s) dans la photo.".format(number_of_faces))

# Chargez l'image dans un objet de la bibliothèque d'images Python afin de pouvoir dessiner dessus et l'afficher.
pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:

    # Imprimez l'emplacement de chaque visage dans cette image. Chaque visage est une liste de coordonnées en (haut, droite, bas, gauche)., left) order.
    top, right, bottom, left = face_location
    print("Un visage est situé à l'emplacement du pixel Haut: {}, gauche: {}, Bas: {}, Droite: {}".format(top, left, bottom, right))

    # Dessinons une boîte autour du visage ou rectangle englobant le visage
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")

# Display the image on screen
pil_image.show()

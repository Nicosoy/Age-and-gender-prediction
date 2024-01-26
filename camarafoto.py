import cv2
import face_recognition
import random
import streamlit as st
st.title("Hello, Model!")

cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido:
    # Detectar caras en el frame capturado
    face_locs = face_recognition.face_locations(frame)

    # Comprobar si se encontró al menos una cara
    if face_locs:
        face_loc = face_locs[0]  # Tomar la primera cara encontrada

        # Coordenadas de la cara
        top, right, bottom, left = face_loc

        # Recortar la imagen a la cara
        face_image = frame[top:bottom, left:right]

        # Generar un número aleatorio del 1 al 1000 para el nombre del archivo
        numero_aleatorio = random.randint(1, 1000)
        nombre_foto_cara = f"foto_cara_{numero_aleatorio}.png"

        # Guardar la imagen recortada de la cara
        cv2.imwrite(nombre_foto_cara, face_image)
        print(f"Foto de la cara {nombre_foto_cara} guardada correctamente")
    else:
        print("No se detectó ninguna cara en la imagen.")

else:
    print("Error al acceder a la cámara")

cap.release()

# Liberar recursos de OpenCV
cv2.destroyAllWindows()

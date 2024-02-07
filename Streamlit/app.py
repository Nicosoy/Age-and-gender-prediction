import streamlit as st
from PIL import Image
import io
import tensorflow as tf
import numpy as np

# Cargar el modelo
model = tf.keras.models.load_model('modelogenero.h5')

def predecir(input_data):
    return model.predict(input_data)

# Personalización con HTML y CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #ff7e5f;
        background-image: linear-gradient(315deg, #ff7e5f 0%, #feb47b 74%);
    }
    .stFileUploader {
        background-color: #ff9966;
        border-color: #ff5e62;
    }
    .file_uploader {
        background-color: #ff9966;
        border-color: #ff5e62;
    }
    .stButton>button {
        color: #fff;
        background-color: #ff5e62;
        border-color: #ff9966;
    }
    .big-font {
        font-size:25px !important;
        font-weight: bold;
    }
    .image-caption {
        text-align: center;
        font-weight: bold;
        color: #fff;
    }
    h1 {
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    .reminder-text {
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
        font-weight: bold;
        color: #000;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Insertar Imagen a Predecir', anchor=None)

# Crear tres columnas
col1, col2, col3 = st.columns([1,2,1])

# Columna izquierda
with col1:
    st.image("columna1.png")  # Reemplazar con la URL o ruta de la imagen

# Columna central
with col2:
    uploaded_file = st.file_uploader("Sube una imagen", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        image = Image.open(io.BytesIO(image_data))
        st.image(image, caption='', use_column_width=True)
        image = image.resize((200, 200))
        img_array = tf.keras.preprocessing.image.img_to_array(image) / 255
        img_array = np.expand_dims(img_array, axis=0)
        predictions = predecir(img_array)

        if predictions[0] < 0.5:
            st.markdown('<p class="big-font">Eres un... HOMBRE!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="big-font">Eres una... MUJER!</p>', unsafe_allow_html=True)

# Mensaje recordatorio
st.markdown('<p class="reminder-text">RECUERDA: El género no lo define una máquina!</p>', unsafe_allow_html=True)

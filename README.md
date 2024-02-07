# Age and Gender Prediction using Deep Learning

Este proyecto utiliza técnicas de Deep Learning para predecir la edad y el género de personas a partir de imágenes faciales. El modelo se desarrolló utilizando la biblioteca Keras y se entrenó con un conjunto de datos de 25,000 imágenes faciales etiquetadas con edad y género.

## Descripción del Proyecto

El objetivo de este proyecto es construir un modelo de aprendizaje profundo que pueda predecir con precisión la edad y el género de una persona a partir de una imagen facial. El modelo se implementa utilizando la arquitectura de red neuronal convolucional (CNN) proporcionada por Keras.

## Conjunto de Datos

El conjunto de datos utilizado en este proyecto consta de 25,000 imágenes faciales etiquetadas con la edad y el género de las personas. Se ha preprocesado y dividido en conjuntos de entrenamiento, validación y prueba para garantizar la efectividad del modelo.

## Tecnologías Utilizadas

- Keras: Biblioteca de Deep Learning que proporciona una interfaz simple y elegante para la construcción y entrenamiento de modelos de aprendizaje profundo.
- TensorFlow: Plataforma de código abierto para machine learning y deep learning, utilizada como backend de Keras.
- Streamlit: Framework de Python para la creación de aplicaciones web interactivas y visualización de datos. Se utiliza para crear una interfaz de usuario amigable donde los usuarios pueden cargar imágenes y obtener las predicciones de edad y género.

## Documentación

La documentacion detalla la teoria, herramientas y funcionalidades del proyecto.
## Estructura del Proyecto

- `data/`: Directorio que contiene el conjunto de datos de imágenes faciales.
- `models/`: Directorio que contiene los modelos preentrenados y los archivos de pesos del modelo.
- `src/`: Directorio que contiene el código fuente del proyecto.
  - `train_model.py`: Script para entrenar el modelo utilizando Keras.
  - `predict.py`: Script para realizar predicciones de edad y género sobre imágenes de entrada.
  - `app.py`: Script principal para la aplicación Streamlit.
- `documentation.md`: Documentación detallada sobre cómo configurar, entrenar y utilizar el modelo, así como sobre cómo ejecutar la aplicación Streamlit.

## Ejecución del Proyecto

1. Clona este repositorio en tu máquina local.
2. Configura el entorno de Python con las dependencias requeridas.
3. Entrena el modelo ejecutando `modelogenero.ipynb`.
4. Ejecuta la aplicación Streamlit utilizando `streamlit run src/app.py`.

¡Disfruta explorando el proyecto y experimentando con la predicción de edad y género a partir de imágenes faciales!

---
*Este proyecto fue desarrollado por Nicolas Martin Diaz como parte del curso 4GeeksAcademy.

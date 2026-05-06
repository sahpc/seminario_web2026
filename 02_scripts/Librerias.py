import pandas as pd  ##permite importar las librerias de pandas ára su utilización
import numpy as np  #Sirve para trabajar con números y arrays (vectores y matrices)
import matplotlib.pyplot as plt  #Sirve para crear gráficos básicos.
import seaborn as sns  # Sirve para visualizaciones estadísticas más avanzadas y bonitas.


# Cargar el dataset
file_path = '/content/drive/MyDrive/Colab Notebooks/SeminarioWeb/Reviews.csv'
df = pd.read_csv(file_path)
df.head()


 from sklearn.metrics import confusion_matrix   #sirve para importar una función que evalúa modelos de Machine Learning, específicamente para ver qué tan bien está clasificando tu modelo.
#1 Instalar dependencias
!pip install vaderSentiment lightgbm -q #vaderSentiment sirve para análisis de sentimiento de texto
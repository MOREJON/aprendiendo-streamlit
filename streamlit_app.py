import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Cargar los datos
@st.cache
def load_data():
    data = pd.read_csv('peliculas.csv')  # Asegúrate de que la ruta al archivo CSV es correcta
    return data

data = load_data()

# Título de la aplicación
st.title('Filtro de Películas')

# Filtros
genre = st.sidebar.multiselect('Seleccione el género:', options=data['Genre'].unique())
director = st.sidebar.multiselect('Seleccione el director:', options=data['Director'].unique())
year = st.sidebar.slider('Seleccione el año:', int(data['Year'].min()), int(data['Year'].max()), (int(data['Year'].min()), int(data['Year'].max())))

# Filtrar datos
filtered_data = data
if genre:
    filtered_data = filtered_data[filtered_data['Genre'].isin(genre)]
if director:
    filtered_data = filtered_data[filtered_data['Director'].isin(director)]
if year:
    filtered_data = filtered_data[(filtered_data['Year'] >= year[0]) & (filtered_data['Year'] <= year[1])]

# Mostrar total de películas
total_movies = len(filtered_data)
st.header(f'Total de Películas Filtradas: {total_movies}')

# Mostrar datos filtrados
st.write('Datos Filtrados', filtered_data)

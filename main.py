import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('features_propiedades_final.csv', index_col=0)
segments_avg = pd.read_csv('promedios_segmentos.csv', index_col=0)

st.header("Cuanto Vale tu Propiedad: General San Martín")
st.text_input("Ingresá tu nombre: ", key="name")

if st.checkbox('Mostrar muestra del set de datos de entrenamiento'):
    df[:30]

st.subheader("Por favor ingresar las caracteristicas de la propiedad:")

left_column, right_column = st.columns(2)
with left_column:
    feature_type = st.radio(
        'Tipo de propiedad:',
        np.unique(df['type']))

st.write('Los diferentes segmentos pueden consultarse en el mapa haciendo [acá](https://www.google.com/maps/d/u/0/edit?mid=1D53sXpkQJc8f3ESd5F4SNj92LI0rsRk&usp=sharing)')

left_column, right_column = st.columns(2)

with left_column:
    feature_price_m2 = st.radio(
        'Segmento donde se encuentra la propiedad:',
        np.unique(segments_avg['area']))

feature_covered_surface_m2 = st.slider('Superficie cubierta en m2', min_value=min(df['covered_surface_m2']), max_value=max(df['covered_surface_m2']), step = 1.0)  
feature_bedrooms = st.slider('Cantidad de dormitorios', min_value=min(df['bedrooms']), max_value=max(df['bedrooms']), step = 1.0)  
feature_bathrooms = st.slider('Cantidad de baños', min_value=min(df['bathrooms']), max_value=max(df['bathrooms']), step = 1.0)  
feature_latitude = st.slider('Latitud en el mapa (aproximada)', min_value=min(df['latitude']), max_value=max(df['latitude']),step=0.0001)  
feature_longitude = st.slider('Longitud en el mapa (aproximado)', min_value=min(df['longitude']), max_value=max(df['longitude']),step=0.0001)  
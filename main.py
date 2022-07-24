import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

regressor_rf = joblib.load('regressor_rf.joblib')
df = pd.read_csv('features_propiedades_final.csv', index_col=0)
segments_avg = pd.read_csv('promedios_segmentos.csv', index_col=0)

st.header("Tasador de propiedades dentro del partido de General San Martín")
st.text_input("Ingresá tu nombre: ", key="name")

if st.checkbox('Mostrar muestra del set de datos de entrenamiento'):
    df.head(20)

st.subheader("Por favor ingresar las caracteristicas de la propiedad!")
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

feature_covered_surface_m2 = st.slider('Superficie cubierta en m2', 0.0, max(df['covered_surface_m2']), 1.0)  
feature_bedrooms = st.slider('Cantidad de dormitorios', 0.0, max(df['bedrooms']), 1.0)  
feature_bathrooms = st.slider('Cantidad de baños', 0.0, max(df['bathrooms']), 1.0)  
feature_latitude = st.slider('Latitud en el mapa', min_value=min(df['latitude']), max_value=max(df['latitude']),step=0.0001)  
feature_longitude = st.slider('Longitud en el mapa', min_value=min(df['longitude']), max_value=max(df['longitude']),step=0.0001)  
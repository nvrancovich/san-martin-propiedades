import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb

xgboost_regressor = xgb.XGBRegressor()
xgboost_regressor.load_model("xgboost_regressor.json")

df = pd.read_csv('propiedades_limpio.csv', index_col=0)
propiety_tipes = {'Casa':'casa', 'Departamento':'departamento', 'Propiedad Horizontal':'ph'}
segments_avg = pd.read_csv('promedios_segmentos.csv', index_col=0,usecols=['area','price/m2'])
segments_centroids = pd.read_csv('segmentos_centroides.csv', index_col=0)
segments_centroids_lat = segments_centroids['latitude'].to_dict()
segments_centroids_lon = segments_centroids['longitude'].to_dict()

st.header("Cuanto Vale tu Propiedad: General San Martín")

if st.checkbox('Ver muestra del set de datos de entrenamiento'):
    df[:30]

st.subheader("Ingresar características de la propiedad:")

left_column, right_column = st.columns(2)
with left_column:
    feature_type = st.radio(
        'Tipo de propiedad:',
        list(propiety_tipes.keys()))


st.write('Los diferentes segmentos pueden consultarse en el mapa tocando [acá](https://www.google.com/maps/d/u/0/edit?mid=1D53sXpkQJc8f3ESd5F4SNj92LI0rsRk&usp=sharing) (tener abierto Google Maps previamente).')

left_column, right_column = st.columns(2)

with left_column:
    feature_segment = st.radio(
        'Segmento donde se encuentra la propiedad:',
        np.unique(segments_avg.index))

feature_covered_surface_m2 = st.slider('Superficie cubierta en m2:', min_value=min(df['covered_surface_m2']), max_value=max(df['covered_surface_m2']), step = 1.0)  
feature_bedrooms = st.slider('Cantidad de dormitorios (0 si es un monoambiente):', min_value=min(df['bedrooms']), max_value=max(df['bedrooms']), step = 1.0)  
feature_bathrooms = st.slider('Cantidad de baños:', min_value=min(df['bathrooms']), max_value=max(df['bathrooms']), step = 1.0)  

feature_latitude = segments_centroids_lat[feature_segment]
feature_longitude = segments_centroids_lon[feature_segment]

if st.button('Hacer predicción'):

    feature_type = propiety_tipes[feature_type]
    if feature_type == 'casa':
        feature_casa = 1
    else:
        feature_casa = 0
    if feature_type == 'departamento':
        feature_dpto = 1
    else:
        feature_dpto = 0
    if feature_type == 'ph':
        feature_ph = 1
    else:
        feature_ph = 0

    feature_price_m2 = segments_avg.to_dict()['price/m2'][feature_segment]

    inputs = np.expand_dims(
        [feature_covered_surface_m2, 
        feature_bedrooms, 
        feature_price_m2,
        feature_bathrooms, 
        feature_latitude, 
        feature_longitude, 
        feature_casa, 
        feature_dpto, 
        feature_ph], 0)

    prediction = float(xgboost_regressor.predict(inputs))
    print('prediction:', round(prediction),-3)
    st.write((f'El valor estimado es de ${int(round(prediction, -3)):,d}.').replace(',','.'))
    st.write(f'¡Gracias por utilizar mi aplicación!')
    st.write(f'Si te gustó, podés seguirme en [Medium](https://medium.com/@nvrancovich) para más contenido similar')
















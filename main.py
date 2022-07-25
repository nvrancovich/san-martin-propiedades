import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb

xgboost_regressor = xgb.XGBRegressor()
xgboost_regressor.load_model("xgboost_regressor.json")

df = pd.read_csv('features_propiedades_final.csv', index_col=0)
propiety_tipes = {'Casa':'casa', 'Departamento':'departamento', 'Propiedad Horizontal':'ph'}
segments_avg = pd.read_csv('promedios_segmentos.csv', index_col=0,usecols=['area','price/m2'])

st.header("Cuanto Vale tu Propiedad: General San Martín")
st.text_input("Ingresá tu nombre: ", key="name")

if st.checkbox('Mostrar muestra del set de datos de entrenamiento'):
    df[:30]

st.subheader("Por favor ingresar las caracteristicas de la propiedad:")

left_column, right_column = st.columns(2)
with left_column:
    feature_type = st.radio(
        'Tipo de propiedad:',
        list(propiety_tipes.keys()))


st.write('Los diferentes segmentos pueden consultarse en el mapa haciendo [acá](https://www.google.com/maps/d/u/0/edit?mid=1D53sXpkQJc8f3ESd5F4SNj92LI0rsRk&usp=sharing)')

left_column, right_column = st.columns(2)

with left_column:
    feature_price_m2 = st.radio(
        'Segmento donde se encuentra la propiedad:',
        np.unique(segments_avg.index))

feature_covered_surface_m2 = st.slider('Superficie cubierta en m2', min_value=min(df['covered_surface_m2']), max_value=max(df['covered_surface_m2']), step = 1.0)  
feature_bedrooms = st.slider('Cantidad de dormitorios', min_value=min(df['bedrooms']), max_value=max(df['bedrooms']), step = 1.0)  
feature_bathrooms = st.slider('Cantidad de baños', min_value=min(df['bathrooms']), max_value=max(df['bathrooms']), step = 1.0)  
feature_latitude = st.slider('Latitud en el mapa (aproximada)', min_value=min(df['latitude']), max_value=max(df['latitude']),step=0.0001)  
feature_longitude = st.slider('Longitud en el mapa (aproximado)', min_value=min(df['longitude']), max_value=max(df['longitude']),step=0.0001)  

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

    feature_price_m2 = segments_avg.to_dict()['price/m2'][feature_price_m2]

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

    prediction = xgboost_regressor.predict(inputs)

    st.write(prediction)














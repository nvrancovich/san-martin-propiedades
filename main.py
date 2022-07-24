import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

regressor_rf = joblib.load('regressor_rf.joblib')
df = pd.read_csv('features_propiedades_final.csv', index_col=0)

st.header("Tasador de casas dentro del partido de General San Martín")
st.text_input("Enter your Name: ", key="name")

if st.checkbox('Show Training Dataframe'):
    df

st.subheader("Please select relevant features of your fish!")
left_column, right_column = st.columns(2)
with left_column:
    feature_type = st.radio(
        'Tipo de propiedad:',
        np.unique(df['Type']))


feature_covered_surface_m2 = st.slider('Superficie cubierta en m2', 0.0, max(df['covered_surface_m2']), 1.0)  
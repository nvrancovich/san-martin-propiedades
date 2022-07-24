import streamlit as st
import pandas as pd
from sklearn.preprocessing import  LabelEncoder
import xgboost as xgb
import numpy as np

st.header("Tasador de casas dentro del partido de General San Martín")
st.text_input("Enter your Name: ", key="name")

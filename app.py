from batch_page import show_batch_page
from predict_page import show_predict_page
from explore_page import show_explore_page
from PIL import Image
import streamlit as st
import joblib
import os

image = Image.open('idea.png')
filename='finalized_model.sav'
location = os.getcwd()
model = joblib.load(f'{location}/{filename}')


selection = st.sidebar.selectbox("Select",("Predict","Batch","Explore"))
st.sidebar.info('This app is created to predict Stack Overflow Survey 2018')
st.sidebar.image(image)
if selection == 'Predict':
    show_predict_page(model)
elif selection == 'Batch':
    show_batch_page(model)
elif selection == 'Explore':
    show_explore_page()
 

			

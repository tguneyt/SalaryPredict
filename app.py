from batch_page import show_batch_page
from predict_page import show_predict_page
from explore_page import show_explore_page
from PIL import Image
import streamlit as st
import joblib
import os

image = Image.open('idea.png')
location = os.getcwd()
# filename=f'{location}\\finalized_model.sav'
filename ='finalized_model.sav'
model = joblib.load(filename)
# print(f'{location}\{filename}')

selection = st.sidebar.selectbox("Choose Operation",("Predict","Batch","Explore"))
st.sidebar.info('This app is created to predict Stack Overflow Survey 2018')
st.sidebar.image(image)

if selection == 'Predict':
    show_predict_page(model)
elif selection == 'Batch':
    show_batch_page(model)
elif selection == 'Explore':
    show_explore_page()
 

			

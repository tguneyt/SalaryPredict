
import streamlit as st
import pandas as pd
from preprocessing import preprocess



def show_batch_page(model):

    
    st.subheader("Dataset upload")
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file,encoding= 'utf-8')
        #Get overview of data
        st.write(data.head())
        st.markdown("<h3></h3>", unsafe_allow_html=True)
        #Preprocess inputs
        preprocess_df = preprocess(data, "Batch")
        btn_predict = st.button('Calculate Salary')
        
        if btn_predict:
            #Get batch prediction
            prediction = model.predict(preprocess_df)
            prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
            # prediction_df = prediction_df.replace({1:'Yes, the passenger survive.', 0:'No, the passenger died'})

            st.markdown("<h3></h3>", unsafe_allow_html=True)
            st.subheader('Prediction')
            st.write(prediction_df)
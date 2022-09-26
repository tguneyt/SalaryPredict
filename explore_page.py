import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objs as go
from plotly.offline import iplot
import seaborn as sns


data = pd.read_csv('data_plt.csv')


def summary_with_graph(dataframe, col_name):
    
    
    st.write(f'### {col_name} Frequency')
    fig1,ax1 =plt.subplots()
    # data= dataframe[col_name].value_counts()
    # ax1.pie(data,labels=data.index, autopct="%1.1f%%",startangle=90,
            
    #         )
    
    data= dataframe[col_name].value_counts()
    # print(data,end='\n\n')
    st.bar_chart(data)
    
    # ax1.axis("equal")
    
    # data = dataframe[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary']
    # st.pyplot(fig1)
    
    st.write(f'### {col_name} Average Salary')
    
    data = dataframe.groupby([col_name])['ConvertedSalary'].mean()
    # print(data)
    st.bar_chart(data)
    
    # st.pyplot(fig1)


def show_explore_page():
    
    st.title('Explore Software Developer Salaries')
    
    st.write('''
             # Stack Overflow Developer Survey 2018
             ''')
    
    st.write('### Which data do you want to see the charts of?')
    column_list = list(data.columns)
    column_list.insert(0,'')
    column_tuple= tuple(column_list)
    
    cart = st.selectbox('',column_tuple)

    
    if cart!='':
        btn_ok = st.button('Show Charts')
        if btn_ok:
            summary_with_graph(data, cart)

import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv('data_plt.csv')


def summary_with_graph(dataframe, col_name):
    
    
    st.write(f'### {col_name} Frequency')
    # fig1,ax1 =plt.subplots()
    # data= dataframe[col_name].value_counts()
    # ax1.pie(data,labels=data.index, autopct="%1.1f%%",startangle=90,
            
    #         )
    
    data= dataframe[col_name].value_counts()
    st.bar_chart(data)
    
    # ax1.axis("equal")
    
    # data = dataframe[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary']
    # st.pyplot(fig1)
    
    average_salary = round((np.mean(dataframe.groupby([col_name])['ConvertedSalary'].mean().to_list())),2)
    st.write(f'### Average Salary for {col_name} Values ')
    st.write(f"Mean for {col_name} : {average_salary}")
    
    data = dataframe.groupby([col_name])['ConvertedSalary'].mean()
    
    st.bar_chart(data)
    
    


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

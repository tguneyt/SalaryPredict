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
    data= dataframe[col_name].value_counts()
    ax1.pie(data,labels=data.index, autopct="%1.1f%%",startangle=90)
    ax1.axis("equal")
    # data = dataframe[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary']
    st.pyplot(fig1)
    
    st.write(f'### {col_name} Average Salary')
    
    data = dataframe.groupby([col_name])['ConvertedSalary'].mean().sort_values(ascending=True)
    
    st.bar_chart(data)
    
    # st.pyplot(fig1)
    # colors = ['#494BD3', '#E28AE2', '#F1F481', '#79DB80', '#DF5F5F',
    #           '#69DADE', '#C2E37D', '#E26580', '#D39F49', '#B96FE3']
    
    # salary_list=dataframe[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary'].to_list()
    # mean_list=[]
    # check=[]
    # for i in range(len(salary_list)):
    #     mean_list.append(np.mean(salary_list))
    

    
    # fig = make_subplots(rows=1, cols=3,
    #                     subplot_titles=('Countplot','Average Salary', 'Percentages'),
    #                     specs=[[{"type": "xy"},{"type": "xy"}, {'type': 'domain'}]])

    # fig.add_trace(go.Bar(y=dataframe[col_name].value_counts().values.tolist(),
    #                      x=[str(i) for i in dataframe[col_name].value_counts().index],
    #                      text=dataframe[col_name].value_counts().values.tolist(),
    #                      textfont=dict(size=15),
    #                      name=col_name,
    #                      textposition='auto',
    #                      showlegend=False,
    #                      marker=dict(color=colors,
    #                                  line=dict(color='#DBE6EC',
    #                                            width=1))),
    #               row=1, col=1)

    # fig.add_trace(go.Bar(y=dataframe[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary'].to_list(),
    #                      x=[str(i) for i in dataframe[col_name].value_counts().index],
    #                  #     text=df[[col_name, 'ConvertedSalary']].groupby([col_name],as_index=False).mean()['ConvertedSalary'].to_list(),
    #                      textfont=dict(size=15),
    #                      name=col_name,
    #                      textposition='auto',
    #                      showlegend=False,
                        
    #                      marker=dict(color=colors,
    #                                  line=dict(color='#DBE6EC',
    #                                            width=1))),
    #               row=1, col=2)

    # fig.add_trace(
    #     go.Scatter( x=[str(i) for i in dataframe[col_name].value_counts().index],
    #             y=mean_list,
                
    #             mode ='lines',
    #             name=f'Average Salary ({col_name}) : {round((mean_list[0]),2)}'
    #             # showlegend= False,
    #             # legendgrouptitle='MEAN'
    #             #   hoverinfo='none'
                  
    #             ),
    #      row=1, col=2
    #     )

    # fig.add_trace(go.Pie(labels=dataframe[col_name].value_counts().keys(),
    #                      values=dataframe[col_name].value_counts().values,
    #                      textfont=dict(size=8),
    #                     #  text=dataframe[col_name].value_counts().keys(),
    #                      textposition='auto',
    #                      showlegend=False,
    #                      name=col_name,
                     
    #                      marker=dict(colors=colors)),
    #               row=1, col=3)

    # fig.update_layout(title={'text': col_name.upper(),
    #                          'y': 0.99,
    #                          'x': 0.5,
    #                          'xanchor': 'center',
    #                          'yanchor': 'top'},
    #                   template='plotly_white')

    # iplot(fig)
    

def show_explore_page():
    
    st.title('Explore Software Developer Salaries')
    
    st.write('''
             # Stack Overflow Developer Survey 2018
             ''')
    
    st.write('### Which data do you want to see the charts of?')
    xdf = list(data.columns)
    xdf.insert(0,'')
    t= tuple(xdf)
    
    cart = st.selectbox('',t)

    
    if cart!='':
        btn_ok = st.button('Show Charts')
        if btn_ok:
            summary_with_graph(data, cart)
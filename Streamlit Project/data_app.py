import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pt
import matplotlib.pyplot as plt
from matplotlib import image 
import seaborn as sns

nav=st.sidebar.radio('Navigation',["Home","About Dataset","Dashboard"])

df=pd.read_csv('diamonds.csv')

if nav=='Home':
    st.title('My Portfolio')
    st.subheader('Hey there... I am Suvakanta Sahoo :man-raising-hand:')
    st.markdown('##### A Data Enthusiast')
    st.markdown('''To be the person whom an organization can always rely on and the one who believes that one's growth is synonymous to the organization’s growth.''')
    st.subheader('Connect with me! :handshake:')
    st.markdown('[_LinkedIn_](https://www.linkedin.com/in/suvakantasahoo/)')
    st.markdown('[_Github_](https://github.com/SuvakantaSahoo)')

if nav=='About Dataset':

    st.header('Diamond Data')
    img=image.imread('diamond.jpg')
    st.image(img)
    
    st.subheader('Data Set')
    row=st.number_input('Select Rows',5,df.shape[0],step=5)
    st.dataframe(df.head(row))
    
    
    num,cat=st.columns(2)
    show_numerical_cols = num.checkbox('Numerical Columns')
    show_categorical_cols = cat.checkbox('Categorical Columns')

    if show_numerical_cols:
     num_cols = df.select_dtypes(include=['float64', 'int64'])
     num.write(num_cols)

    if show_categorical_cols:
     cat_cols = df.select_dtypes(include=['category'])
     cat.write(cat_cols)
    
    
    sis=st.selectbox('Get more informations',['None','Shape','Get_info','Statistics'])
    
    if sis=='None':
     pass
    
    if sis=='Shape':
     st.write('Shape of the dataset :',df.shape)
    
    if sis=='Get_info':
     st.write("- Number of Rows:", df.shape[0])
     st.write("- Number of Columns:", df.shape[1])
     st.write("- Columns:", list(df.columns))
     
    if sis=='Statistics':
     stats=df.describe()
     st.write(stats)
     

if nav=='Dashboard':
    
    st.header('Diamond Dashboard')
   
    st.markdown('### Numerical Based Plot')
    num_features=['price','depth','table','x','y','z']
    fig1=st.selectbox('Histogram :',num_features)
    fig1= px.histogram(df[fig1],height=350,width=800)
    st.plotly_chart(fig1, use_container_width=True)
        
    fig2=st.multiselect('Box Plot :',num_features)
    fig2= px.box(df,y=fig2)
    st.plotly_chart(fig2, use_container_width=True)
        
    st.markdown('### Categorical Based Plot')
    fd=st.radio('Count Plot :',['Cut','Color','Clarity'])
    if fd=='Cut':
        fig3= px.histogram(df['cut'],height=350,width=800)
        st.plotly_chart(fig3, use_container_width=True)
    if fd=='Color':
        fig4= px.histogram(df['color'],height=350,width=800)
        st.plotly_chart(fig4, use_container_width=True)
    if fd=='Clarity':
        fig5= px.histogram(df['clarity'],height=350,width=800)
        st.plotly_chart(fig5,color="continent", use_container_width=True)

    st.markdown('### Numeric to Numeric')
    st.markdown('##### Scatter Plot')
    data= [go.Scatter(x=df['carat'],y=df['price'],mode='markers')]
    layout=go.Layout(title='Price vs Carat',xaxis=dict(title='Carat'),yaxis=dict(title='Price'))
    fig6=go.Figure(data=data,layout=layout)
    st.plotly_chart(fig6,color="continent",height=350,width=800,use_container_width=True)
        
    st.markdown('### Numeric to Catagorical')
    st.markdown('##### Bar Chart')
    X=st.radio('Pick Variable :',['cut','color','clarity'])
    fig7,ax=plt.subplots(figsize=(10,5))
    p=sns.barplot(x=X,y='price',data=df,color='green')
    p.set_title(f"Price vs {X}", fontsize = 20,color='r')
    st.pyplot(fig7)

    st.markdown('##### Box Plot')
    bp=st.radio('Choose Variable :',['cut','color','clarity'])
    fig8 = px.box(df, x =bp, y="carat", points="all")
    fig8.update_traces(quartilemethod="inclusive")
    st.plotly_chart(fig8,height=500,width=1000,use_container_width=True)
        
    st.markdown('### Tree Map')
    tm=st.radio('Tree Feature :',['price','carat'])
    fig9 = px.treemap(df, path=['cut', 'color', 'clarity'],values=tm,color=tm)
    st.plotly_chart(fig9,color="continent",height=500,width=1000)

    st.markdown('### Heat Map')
    fig10,ax=plt.subplots(figsize=(10,5))
    sns.heatmap(data=df.corr(),annot=True)
    st.pyplot(fig10)



    

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

# Page config
st.set_page_config(
    page_title='Streamlit Features Demo',
    page_icon='🎈',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Title and introduction
st.title('🎈 Streamlit Features Demonstration')
st.markdown('''
This app showcases various Streamlit features including widgets, layouts, charts, and more.
Use the sidebar to navigate through different sections!
''')

# Sidebar navigation
page = st.sidebar.radio('Navigation', 
    ['Basic Elements', 'Data Display', 'Charts & Plots', 'Advanced Features'])

# Basic Elements Section
if page == 'Basic Elements':
    st.header('Basic Elements')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Text Input & Buttons')
        user_name = st.text_input('Enter your name')
        if st.button('Say Hello'):
            st.write(f'Hello, {user_name}! 👋')
            
        st.subheader('Checkboxes & Radio')
        if st.checkbox('Show secret message'):
            st.write('🤫 This is a secret message!')
            
        favorite_color = st.radio(
            'What\'s your favorite color?',
            ['Red', 'Green', 'Blue']
        )
        st.write(f'Your favorite color is {favorite_color}')
    
    with col2:
        st.subheader('Sliders & Selectbox')
        age = st.slider('How old are you?', 0, 100, 25)
        st.write(f'I\'m {age} years old')
        
        option = st.selectbox(
            'How would you like to be contacted?',
            ['Email', 'Phone', 'Mobile']
        )
        st.write(f'You selected: {option}')

# Data Display Section
elif page == 'Data Display':
    st.header('Data Display Features')
    
    # Generate sample data
    df = pd.DataFrame(
        np.random.randn(10, 4),
        columns=['A', 'B', 'C', 'D']
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('DataFrame Display')
        st.dataframe(df.style.highlight_max(axis=0))
        
        st.subheader('Metrics')
        col3, col4, col5 = st.columns(3)
        col3.metric('Temperature', '70 °F', '1.2 °F')
        col4.metric('Wind', '9 mph', '-8%')
        col5.metric('Humidity', '86%', '4%')
    
    with col2:
        st.subheader('JSON Display')
        st.json({
            'name': 'John Doe',
            'age': 30,
            'city': 'San Francisco'
        })
        
        st.subheader('Code Block')
        st.code('''
        def hello_world():
            print('Hello, World!')
        ''')

# Charts & Plots Section
elif page == 'Charts & Plots':
    st.header('Charts & Plots')
    
    # Generate sample data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Line 1', 'Line 2', 'Line 3']
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Line Chart')
        st.line_chart(chart_data)
        
        st.subheader('Bar Chart')
        st.bar_chart(chart_data)
    
    with col2:
        st.subheader('Plotly Chart')
        fig = px.scatter(
            chart_data, 
            title='Interactive Scatter Plot'
        )
        st.plotly_chart(fig)
        
        st.subheader('Area Chart')
        st.area_chart(chart_data)

# Advanced Features Section
elif page == 'Advanced Features':
    st.header('Advanced Features')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('File Uploader')
        uploaded_file = st.file_uploader('Choose a file')
        if uploaded_file is not None:
            st.write('File uploaded successfully!')
            
        st.subheader('Color Picker')
        color = st.color_picker('Pick a color', '#00f900')
        st.write('The selected color is', color)
    
    with col2:
        st.subheader('Progress Bar')
        if st.button('Start Progress'):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            st.success('Done!')
        
        st.subheader('Date Input')
        d = st.date_input(
            'When\'s your birthday',
            datetime.now()
        )
        st.write('Your birthday is:', d)

# Footer
st.sidebar.markdown('---')
st.sidebar.markdown('Made with ❤️ using Streamlit')
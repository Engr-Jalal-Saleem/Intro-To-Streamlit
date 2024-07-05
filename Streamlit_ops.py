import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime
import time
import datetime

st.title('Streamlit Operations')
st.write('This is a simple Streamlit app to perform basic operations')

st.title('DAY 1')
#header
st.header('st.button')

if st.button('Say Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.title('DAY 2')
#example 01
st.write('Hello, *World!* :sunglasses:')
#example 02
st.write(1234)

#example 03 Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

#example 04
st.write('Below is a dataframe:', df, 'Above is a dataframe.')

#example 05
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)

#Furthur Reading
st.header('Further Reading')
st.subheader('Markdown') #Subheader
st.markdown('---')
st.markdown('### Markdown')

st.caption('This is a caption')
st.code('import numpy as np')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.markdown('---')

st.title('DAY 3')
#header
st.header('st.slider')
st.subheader("What we're building?")
st.write('''A simple app that shows the various ways on how to accept user input by adjusting the slider widget.

Flow of the app:

User selects value by adjusting the slider widget
App prints out the selected value''')

#Code
#Slider
st.subheader('Slider')
age = st.slider('How old are you?', 0,130,25)
st.write(f'I am {age} years old.')
st.subheader('Code')
st.code('''#Slider
st.subheader('Slider')
age = st.slider('How old are you?', 0,130,25)
st.write(f'I am {age} years old.')''')
st.markdown('---')

#Range Slider
st.subheader('Range Slider')
values = st.slider('Select a range of values', 0.0,100.0,(25.0,50.0))
st.write(f'Values selected: {values}')
st.subheader('Code')
st.code('''st.subheader('Range Slider')
values = st.slider('Select a range of values', 0.0,100.0,(25.0,50.0))
st.write(f'Values selected: {values}')''')
st.markdown('---')

#Range Time Slider
st.subheader('Range Time Slider')
apptmnt = st.slider('Schedule your appointment:', value=(datetime.time(8,45,15), datetime.time(9,0,0)))
st.write('You have an appointment at:', apptmnt)
st.subheader('Code')
st.code('''#Range Time Slider
st.subheader('Range Time Slider')
apptmnt = st.slider('Schedule your appointment:', value=(datetime.time(8,45,15), datetime.time(9,0,0)))
st.write('You have an appointment at:', apptmnt)''')
st.markdown('---')

#Date Time Slider
st.subheader('Date Time Slider')
start_time = st.slider('When do you start?',value=datetime.datetime(2020,1,1,9,30),format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)
st.write('Start time:', start_time.strftime('%Y-%m-%d %H:%M:%S'))
st.subheader('Code')
st.code('''#Date Time Slider
st.subheader('Date Time Slider')
start_time = st.slider('When do you start?',value=datetime.datetime(2020,1,1,9,30),format='MM/DD/YY - hh:mm')
st.write('Start time:', start_time)
st.write('Start time:', start_time.strftime('%Y-%m-%d %H:%M:%S'))''')
st.markdown('---')

#Select Slider
st.header('Further Reading')
st.subheader('Select Slider')
start_color , end_color = st.select_slider('Select a range of color', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo','violet'],value=('red','blue'))
st.write('You selected wavelengths between :', start_color, 'and', end_color)
st.subheader('Code')
st.code('''#Select Slider
st.subheader('Select Slider')
start_color , end_color = st.select_slider('Select a range of color', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo','violet'],value=('red','blue'))
st.write('You selected wavelengths between :', start_color, 'and', end_color)''')
st.markdown('---')
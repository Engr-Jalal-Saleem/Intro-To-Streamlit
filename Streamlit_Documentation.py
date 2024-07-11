import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime
import time
import datetime
import json
from pathlib import Path
# st.set_page_config(layout="wide")

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




st.title('Day 4')
st.header('st.line_chart')
st.subheader("What we're building?")
st.write('''A simple app for displaying a line chart.

Flow of the app:

Create a Pandas DataFrame from numbers randomly generated via NumPy.
Create and display the line chart via st.line_chart() command.''')
st.header('Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)
st.subheader('Code')
st.code('''st.header('Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)''')
st.markdown('---')

st.title('Day 5')
st.header('st.selectbox')
st.subheader("What we're building?")
st.write('''A simple app that asks the user what their favorite color is.

Flow of the app:

User selects a color
App prints out the selected color''')

st.header('st.selectbox')
option = st.selectbox(
    'What is your Favourite Color:',
    ('Blue','Red','Green')
)
st.write('My favourite color is :', option)
st.subheader('Code')
st.code('''
st.header('st.selectbox')
option = st.selectbox(
    'What is your Favourite Color:',
    ('Blue','Red','Green')
)
st.write('My favourite color is :', option)''')
st.markdown('---')

st.subheader('Further Reading')
st.write('''Select widgets can customize how to hide their labels with the label_visibility parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to label=""). If "collapsed", both the label and the space are removed. Default is "visible". Select widgets can also be disabled with the disabled parameter''')

st.subheader('label_visibility')
if "visibility" not in st.session_state:
    st.session_state.visibility = 'visible'
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox('Disable SelectBox widget.', key='disabled')
    st.radio(
        'Set Selectbox label visibilty 👉',
        key = 'visibility',
        options=['visible', 'hidden','collapsed'],
    )
with col2:
    option = st.selectbox(
        'How would you like to be connected?',
        ("Email",'Phone', 'WhatsApp'),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.subheader('Code')
st.code('''st.subheader('label_visibility')
if "visibility" not in st.session_state:
    st.session_state.visibility = 'visible'
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox('Disable SelectBox widget.', key='disabled')
    st.radio(
        'Set Selectbox label visibilty 👉',
        key = 'visibility',
        options=['visible', 'hidden','collapsed'],
    )
with col2:
    option = st.selectbox(
        'How would you like to be connected?',
        ("Email",'Phone', 'WhatsApp'),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
''')
st.markdown('---')

#Day 06
st.title('Day 06')
st.header('st.multiselect')
st.write('st.multiselect displays a multiselect widget.')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You Selected', options)
st.subheader('Code')
st.code('''st.header('st.multiselect')
st.write('st.multiselect displays a multiselect widget.')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('You Selected', options)''')
st.markdown('---')

#Day 07
st.title('Day 07')
st.header('st.checkbox')
st.write('st.checkbox displays a checkbox widget.')

st.subheader('CheckBox')
st.write('What would you like to order?')
ice_cream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if ice_cream:
    st.write("Great! Here's some more 🍦")

if coffee: 
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")
    
st.subheader('Code')
st.code('''st.subheader('CheckBox')
st.write('What would you like to order?')
ice_cream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if ice_cream:
    st.write("Great! Here's some more 🍦")

if coffee: 
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")
    
st.subheader('Code')''')
st.markdown('---')

#Day 08
st.title('Day 08')
st.header('Streamlit Components')
st.subheader('What Streamlit components are available?')
st.write('''There are several dozens of Streamlit components featured on Streamlit's website [2].

Fanilo (a Streamlit Creator) curated an amazing list of Streamlit components on a wiki post [3] that lists about 85 Streamlit components as of April 2022.''')
st.subheader('How to use?')
st.write('''Streamlit components are just a pip-install away.

In this tutorial, let's get you started in using the streamlit_pandas_profiling component [4].''')
st.subheader('Install the component')
st.code('pip install streamlit_pandas_profiling')









#Day 09
st.title('DAY 09')
st.header('st.latex')
st.subheader('What we are building?')
st.write('A simple app that shows how to use the st.latex function to render mathematical expressions in Streamlit.')

st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
''')
st.subheader('Code')
st.code('''st.latex(r
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
)''')
st.markdown('---')

#Day 10
st.title('DAY 10')
st.header('Customizing the theme of Streamlit apps')
st.subheader('What we are building?')
st.write('A simple app that shows the result of our theme customization. This is made possible by customizing the HTML HEX code inside the `.streamlit/config.toml` file.')
st.write('Contents of the `.streamlit/config.toml` file of this app')
st.subheader('Code')
st.code('''
        [theme]
        primaryColor="#E694FF"
        backgroundColor="#00172B"
        secondaryBackgroundColor="#0085CA"
        textColor="#FFFFFF"
        font="sans serif"
''')
number = st.sidebar.slider('Pick a number', 0, 100)
st.write('You selected:', number)
st.markdown('---')

#Day 11
st.title('DAY 11')
st.header('st.secrets')
st.write('`st.secrets` allows you to store confidential information such as API keys, database passwords or other credentials.')
st.write(st.secrets['message'])
st.write('Note: You need to create a `secrets.toml` file in the root directory of your Streamlit app and add the secret key-value pair in it.')
st.subheader('Code')
st.code('''st.write(st.secrets['message'])''')
st.markdown('---')


#Day 12
st.title('DAY 12')
st.header('st.file_uploader')
st.write('''`st.file_uploader` displays a file uploader widget.

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option.''')
st.subheader('Input CSV file')
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
else:
    st.info('☝️ Upload a CSV file')
st.subheader('Code')
st.code('''
        uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data)
        else:
            st.info('☝️ Upload a CSV file')
''')
st.markdown('---')

#Day 13
st.title('DAY 13')
st.header('How to layout your Streamlit app')
st.write('''
        In this tutorial, we're going to use the following commands to layout our Streamlit app:

`st.set_page_config(layout="wide")` - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.

`st.sidebar` - Places the widgets or text/image displays in the sidebar.

`st.expander` - Places text/image displays inside a collapsible container box.

`st.columns` - Creates a tabular space (or column) within which contents can be placed inside.
''')
st.markdown('---')
st.subheader('st.set_page_config')
# st.set_page_config(layout="wide")
st.write('''`set_page_config()` can only be called once per app page, and must be called as the first Streamlit command in your script.''')
# st.write('This is a wide mode Streamlit app')
st.subheader('Code')
st.code('''st.set_page_config(layout="wide")''')
st.markdown('---')

st.subheader('st.expander')
with st.expander('About The Coder!'):
    st.write('''I'm Engr. Jalal Saleem, a passionate student with a kaleidoscope of skills. My journey through tech and design has painted me with a unique blend of analytical precision and creative flair. I don't just crunch data; I turn it into a compass, guiding campaigns to their true north and illuminating the path to informed decisions. As an Electrical Engineering student, I see beyond circuits—I see complex systems that have taught me to untangle even the most knotted problems. I'm not just eager to collaborate; I'm excited to weave my thread into the tapestry of innovative projects that leave a lasting impact. Let's not just innovate—let's create a masterpiece together!''')
    st.image(
        r'c:\Users\jalal\Downloads\IMG_3045.jpg',
        caption='This is Engr. Jalal Saleem, who made this app',
        use_column_width=True
    )

st.subheader('Code')
st.code('''
        st.subheader('st.expander')
with st.expander('About This App!'):
    st.write('This is a simple Streamlit app to layout the contents of the app in wide mode.')
    st.image(
        'Add Image URL here',
        caption='This is Engr. Jalal Saleem, who made this app',
        use_column_width=True
    )''')
st.markdown('---')

st.subheader('st.sidebar.header & st.columns()')
user_name = st.sidebar.text_input('Enter your name')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')
#Code for st.columns
col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')

st.subheader('Code')
st.code('''
        st.subheader('st.sidebar.header')
user_name = st.sidebar.text_input('Enter your name')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')

''')
st.markdown('---')

#Day 14
st.title('DAY 14')
st.header('st.progress')
st.write('`st.progress` displays a progress bar that updates graphically as the iteration progresses.')

with st.expander('About st.progress'):
    st.write('`st.progress` is a simple way to display a progress bar that updates graphically as the iteration progresses. It is useful when you want to show the progress of a long-running computation or a loop.')
my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.01)
  my_bar.progress(percent_complete + 1)
# st.balloons()

st.subheader('Code')
st.code('''my_bar = st.progress(0)
for percent_complete in range(100):
  time.sleep(0.09)
  my_bar.progress(percent_complete + 1)
st.balloons()''')
st.markdown('---')
st.subheader('Further Reading')
st.header('st.spinner')
st.write('`st.spinner` displays a spinner widget that indicates a computation is in progress.')
with st.expander('About st.spinner'):
    st.write('`st.spinner` is a simple way to display a spinner widget that indicates a computation is in progress. It is useful when you want to show the user that something is happening in the background.')
with st.spinner('Wait for it...'):
  time.sleep(1)# Wait for 1 seconds
st.success('Done!')
st.subheader('Code')
st.code('''with st.spinner('Wait for it...'):
  time.sleep(5)''')
st.markdown('---')

#Day 15
st.title('DAY 15')
st.header('st.form')
st.write('`st.form` is a way to organize your widgets in a form layout. It allows you to group related widgets together and submit them all at once.')
st.text('''Forms have a few constraints:

Every form must contain a `st.form_submit_button`.
`st.button` and `st.download_button` cannot be added to a form.
Forms can appear anywhere in your app (sidebar, columns, etc), but they cannot be embedded inside other forms.''')

st.subheader('1. Example of using `with` notation.')
st.subheader('Coffee Machine')

with st.form(key='my_form'):
  st.subheader('**Order Your Coffee**')
  cof_bean_val = st.selectbox('Select Coffee Beans',['Arabica','Robusta'])
  cof_type_val = st.selectbox('Select Coffee Type',['Espresso','Americano','Latte','Cappuccino'])
  cof_roast_val = st.selectbox('Select Coffee Roast',['Light','Medium','Dark'])
  brewing_val = st.selectbox('Select Brewing Method',['Drip','French Press','Espresso Machine','Aeropress','Siphon'])
  milk_val = st.selectbox('Select Milk Type',['Whole Milk','2% Milk','Almond Milk','Oat Milk','Soy Milk'])  
  suger_val = st.slider('Select Sugar Level',0,10,5,1)
  own_cup_val = st.checkbox('Bring your own cup')
  submit_button = st.form_submit_button(label='Place Order')

  if submit_button:
    st.write('**Order Summary**')
    st.markdown(f'''
                ☕ You have ordered:
                - Coffee Beans: `{cof_bean_val}`
                - Coffee Type: `{cof_type_val}`
                - Coffee Roast: `{cof_roast_val}`
                - Brewing Method: `{brewing_val}`
                - Milk Type: `{milk_val}`
                - Sugar Level: `{suger_val}`
                - Own Cup: `{own_cup_val}`
                ''')

  else:
    st.write('👈 Please fill out the form and submit your order.')

st.subheader('Code')
st.code('''
        with st.form(key='my_form'):
  st.subheader('**Order Your Coffee**')
  cof_bean_val = st.selectbox('Select Coffee Beans',['Arabica','Robusta'])
  cof_type_val = st.selectbox('Select Coffee Type',['Espresso','Americano','Latte','Cappuccino'])
  cof_roast_val = st.selectbox('Select Coffee Roast',['Light','Medium','Dark'])
  brewing_val = st.selectbox('Select Brewing Method',['Drip','French Press','Espresso Machine','Aeropress','Siphon'])
  milk_val = st.selectbox('Select Milk Type',['Whole Milk','2% Milk','Almond Milk','Oat Milk','Soy Milk'])  
  suger_val = st.slider('Select Sugar Level',0,10,5,1)
  own_cup_val = st.checkbox('Bring your own cup')
  submit_button = st.form_submit_button(label='Place Order')

  if submit_button:
    st.write('**Order Summary**')
    st.markdown(f
                You have ordered:
                - Coffee Beans: `{cof_bean_val}`
                - Coffee Type: `{cof_type_val}`
                - Coffee Roast: `{cof_roast_val}`
                - Brewing Method: `{brewing_val}`
                - Milk Type: `{milk_val}`
                - Sugar Level: `{suger_val}`
                - Own Cup: `{own_cup_val}`'
                )

  else:
    st.write('👈 Please fill out the form and submit your order.')
''')
st.markdown('---')
# Short example of using an object notation
st.subheader('2. Example of using object notation.')
st.subheader('Order Your Pizza')

form = st.form(key='Pizza Form')
st.subheader('**Order Your Pizza**')
pizza_size = form.selectbox('Select Pizza Size',['Small','Medium','Large'])
pizza_type = form.selectbox('Select Pizza Type',['Margherita','Pepperoni','Hawaiian','Meat Lovers','Veggie Supreme'])
pizza_crust = form.selectbox('Select Pizza Crust',['Thin Crust','Regular Crust','Thick Crust'])
pizza_toppings = form.multiselect('Select Pizza Toppings',['Extra Cheese','Mushrooms','Pepperoni','Olives','Onions','Bell Peppers'])
extra_sauce = form.checkbox('Extra Sauce')
submit_button = form.form_submit_button(label='Place Order')
if submit_button:
  st.write('**Order Summary**')
  st.markdown(f'''
              🍕 You have ordered:
              - Pizza Size: `{pizza_size}`
              - Pizza Type: `{pizza_type}`
              - Pizza Crust: `{pizza_crust}`
              - Pizza Toppings: `{pizza_toppings}`
              - Extra Sauce: `{extra_sauce}`
              ''')
  st.spinner('Placing your order...')
  time.sleep(5)
else:
  st.write('👈 Please fill out the form and submit your order.')

st.subheader('Code')
st.code('''
        # Short example of using an object notation
st.subheader('2. Example of using object notation.')
st.subheader('Order Your Pizza')

form = st.form(key='Pizza Form')
st.subheader('**Order Your Pizza**')
pizza_size = form.selectbox('Select Pizza Size',['Small','Medium','Large'])
pizza_type = form.selectbox('Select Pizza Type',['Margherita','Pepperoni','Hawaiian','Meat Lovers','Veggie Supreme'])
pizza_crust = form.selectbox('Select Pizza Crust',['Thin Crust','Regular Crust','Thick Crust'])
pizza_toppings = form.multiselect('Select Pizza Toppings',['Extra Cheese','Mushrooms','Pepperoni','Olives','Onions','Bell Peppers'])
extra_sauce = form.checkbox('Extra Sauce')
submit_button = form.form_submit_button(label='Place Order')
if submit_button:
  st.write('**Order Summary**')
  st.markdown(f
              🍕 You have ordered:
              - Pizza Size: `{pizza_size}`
              - Pizza Type: `{pizza_type}`
              - Pizza Crust: `{pizza_crust}`
              - Pizza Toppings: `{pizza_toppings}`
              - Extra Sauce: `{extra_sauce}`
              )
  st.spinner('Placing your order...')
  time.sleep(5)
else:
  st.write('👈 Please fill out the form and submit your order.')
        ''')
st.markdown('---')

#Day 16
st.title('DAY 16')
st.header('Build a draggable and resizable dashboard with Streamlit Elements')
st.subheader('How to use?')
st.write('**Installation**')
st.write('The first step is to install Streamlit Elements in your environment:')
st.code('pip install streamlit-elements')
st.subheader('What we are building?')
st.write('''The goal of today's challenge is to create a dashboard composed of three Material UI cards:

A first card with a Monaco code editor to input some data ;
A second card to display that data in a Nivo Bump chart ;
A third card to show a YouTube video URL defined with a `st.text_input.`''')


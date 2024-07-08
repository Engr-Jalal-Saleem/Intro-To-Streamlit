import streamlit as st

st.title('Final Project')
st.write("In this tutorial, we're going to put our newfound knowledge from this learning challenge to create Streamlit apps to solve real-world problems.")

st.header('Real-world problem')
st.write('''As a content creator, having access to thumbnail images from YouTube videos are useful resources for social promotion and content creation.

Let's figure out how we're going to tackle this problem and build a Streamlit app.''')

st.header('Solution')
st.write('''Today, we're going to build `yt-img-app`, which is a Streamlit app that can extract thumbnail images from YouTube videos.

In a nutshell, here are the 3 simple steps that we want the Streamlit app to do:

1. Accept a YouTube URL as input from users.
2. Perform text processing of the URL to extract the unique YouTube video ID.
3. Use the YouTube video ID as an input to a custom function that retrieves and displays the thumbnail image from YouTube videos.''')

st.header('Instructions')
st.write('To get started in using the Streamlit app, copy and paste a YouTube URL into the input text box.')

st.title('🖼️ YouTube Thumbnail Generator')
st.header('YouTube Thumbnail Image Extractor App')
with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]
yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
    ytid = None
    if 'youtu.be' in input_url:
        ytid = input_url.split('/')[-1]
    elif 'youtube.com' in input_url:
        ytid = input_url.split('v=')[-1].split('&')[0]
    return ytid

if yt_url:
    ytid = get_ytid(yt_url)
    if ytid:
        yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
        st.image(yt_img)
        st.write('YouTube video thumbnail image URL: ', yt_img)
    else:
        st.write('Invalid YouTube URL.')
else:
    st.write('☝️ Enter URL to continue ...')

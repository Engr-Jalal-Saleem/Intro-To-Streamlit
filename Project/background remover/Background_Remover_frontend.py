import streamlit as st
import rembg as bg
from PIL import Image
from io import BytesIO
import base64
st.set_page_config(page_title="Background Remover", layout="wide")

st.sidebar.title("Upload Image")
st.title("Background Remover")
st.markdown("This app uses the rembg library to remove the background of an image. Upload an image and the app will remove the background for you.")


def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    bytes_im = buf.getvalue()
    return bytes_im

def fix_image(uploaded_image):
    image = Image.open(uploaded_image)
    col1.write("Original Image")
    col1.image(image, use_column_width=True)
    fixed = bg.remove(image)
    col2.write("Background Removed Image")
    col2.image(fixed, use_column_width=True)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download Image", convert_image(fixed), "background_removed.png", "Click here to download the image")


col1, col2 = st.columns(2)
uploaded_image = st.sidebar.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
if uploaded_image:
    fix_image(uploaded_image)












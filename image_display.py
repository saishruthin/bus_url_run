import streamlit as st
def image_display(image_path):
    from PIL import Image
    image = Image.open(image_path)
    st.image(image, width = 700)
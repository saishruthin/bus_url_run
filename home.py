import streamlit as st
from image_display import image_display
def home():
    st.title("TSRTC 🚎")
    image_display("home_logo.png")
    st.markdown("#### History")
    with open("history.txt", 'r') as file:
        st.write(file.read())
    st.markdown("### TSRTC Bus fleets: ")
    with open("busfleet.txt", 'r') as file:
        st.write(file.read())
    
home()

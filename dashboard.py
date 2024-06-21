import streamlit as st
from streamlit_option_menu import option_menu
from data import data
from home import home
from image_display import image_display as ig

def aboutus():
    st.header("About Us: ")
    ig("logo2.jpg")
    with open("aboutus.txt", 'r') as file:
        st.write(file.read())
def contactus():
    st.header("Contact us : ")
    with open("contactus.txt", 'r') as file:
        st.write(file.read())


sidebar_style = """
<style>
[data-testid = "stSidebar"]{
backgroud-color: #000000;
}
</style>

"""
st.markdown(sidebar_style, unsafe_allow_html=True)

with st.sidebar:
    option = option_menu(
        menu_title = "Swecha organisation",
        options= ["Data", "Home", "About us: ", "Contact us: "],
        icons = ["house", "file-bar-graph-fill", "file-person", "person-rolodex"],
        menu_icon = "people"
    )
if option == "Home":
    home()
elif option == "Data":
    data()
elif option == "About us: ":
    aboutus()
elif option == "Contact us: ":
    contactus() 
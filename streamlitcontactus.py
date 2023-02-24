import streamlit as st
from PIL import Image
import base64
import streamlit as st

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image_file.jpeg')    

def main():
    # Create a banner at the top with links to other pages
    with st.container():
        st.markdown(
            """
            <div style='background-color: white; padding: 1px;'>
            <h1 style='font-family:Optima;color: #8B4513; text-align: center;'>Jorge & Jeff</h1>
            <p style='font-family: Optima;color: #8B4513; text-align: center; font-size: 20px;'> 
            <a style='color: #8B4513; text-decoration: none;' href='/'>Homepage</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='/clothing'>Clothing</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='/about'>About</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://georginapalmer-teampage-teampage-1k7d1b.streamlit.app' target='_blank'>Team</a>
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
if __name__ == '__main__':
     main()

#contact us: 
contact_title = '<p style="font-family:Optima; color:Black; font-size: 60px;">Contact us:</p>'
st.markdown(contact_title, unsafe_allow_html=True)
phone_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Phone us: 07878882575</p>'
st.markdown(phone_title, unsafe_allow_html=True)
email_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Email us: jjclothing@gmail.com</p>'
st.markdown(email_title, unsafe_allow_html=True)
image = Image.open('jjclothing.jpeg')
st.image(image)


#where to find us? 
findus_title = '<p style="font-family:Optima; color:Black; font-size: 60px;">Find us at: </p>'
st.markdown(findus_title, unsafe_allow_html=True)
findusat_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">95 Oxford Street,DN32 7JE</p>'
st.markdown(findusat_title, unsafe_allow_html=True)
image1 = Image.open('jjclothingplace.jpg')
st.image(image1, caption='95 Oxford Street,DN32 7JE')


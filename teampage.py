import streamlit as st
from PIL import Image
import cv2
import numpy as np
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

image2 = Image.open('JorgeJeff.jpg')
st.image(image2)

#Meet the team: 
meetus_title = '<p style="font-family:Optima; color:Black; font-size: 60px;">Meet the team:</p>'
st.markdown(meetus_title, unsafe_allow_html=True)


Ewan_title = '<strong><p style="font-family:Optima; color:#17304A; font-size: 42px;">Ewan Yeo</p></strong>'
st.markdown(Ewan_title, unsafe_allow_html=True)
roleewan_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Role: Jorge Santos</p>'
st.markdown(roleewan_title, unsafe_allow_html=True)
image3 = Image.open('Ewan.jpeg')
st.image(image3, caption='Ewan Yeo 2023')

Rajat_title = '<strong><p style="font-family:Optima; color:#17304A; font-size: 42px;">Rajat Khole</p></strong>'
st.markdown(Rajat_title, unsafe_allow_html=True)
rolerajat_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Role: Jeff Bridges</p>'
st.markdown(rolerajat_title, unsafe_allow_html=True)
image4 = Image.open('Rajat.jpeg')
st.image(image4, caption='Rajat Khole 2023')

Ethan_title = '<strong><p style="font-family:Optima; color:#17304A; font-size: 42px;">Ethan Woolley</p></strong>'
st.markdown(Ethan_title, unsafe_allow_html=True)
roleethan_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Role: CTO </p>'
st.markdown(roleethan_title, unsafe_allow_html=True)
image5 = Image.open('Ethan.jpeg')
st.image(image5, caption='Ethan Woolley 2023')

Charlotte_title = '<strong><p style="font-family:Optima; color:#17304A; font-size: 42px;">Charlotte Guillemot</p></strong>'
st.markdown(Charlotte_title, unsafe_allow_html=True)
rolecharlotte_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Role: Creative director </p>'
st.markdown(rolecharlotte_title, unsafe_allow_html=True)
image6 = Image.open('Charlotte.jpeg')
st.image(image6, caption='Charlotte Guillemot 2023')

Georgina_title = '<strong><p style="font-family:Optima; color:#17304A; font-size: 42px;">Georgina Palmer</p></strong>'
st.markdown(Georgina_title, unsafe_allow_html=True)
rolegeorgina_title = '<p style="font-family:Optima; color:#17304A; font-size: 42px;">Role: CFO </p>'
st.markdown(rolegeorgina_title, unsafe_allow_html=True)
image7 = Image.open('georgina.jpeg')
st.image(image7, caption='Georgina Palmer 2023')
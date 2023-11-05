# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:11:31 2023

@author: Shrir
"""

import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu", #required
        options=["Home","Image Capture","Image Upload","Contact"], #required
        icons=["house", "camera","cloud-arrow-up","envelope"], #optional
        menu_icon="cast", #optional
        default_index=0, #optional

        )
    st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #b90e0a;
    }
</style>
""", unsafe_allow_html=True)

if selected == "Home":
    st.title(f"You have selected {selected}")
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-color: #000000;
    opacity: 1;
    background-image:  radial-gradient(#ffffff 0.9500000000000001px, transparent 0.9500000000000001px), radial-gradient(#ffffff 0.9500000000000001px, #000000 0.9500000000000001px);
    background-size: 38px 38px;
    background-position: 0 0,19px 19px;
        }
    </style>
    """
    st.markdown("", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: orangered;'> 👂Hear-2-See 👀</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white;'> 🌟 Bridging the Gap Between Sight and Sound 🌟</h4>", unsafe_allow_html=True)
    st.divider()

    with st.expander(" 'Unlocking a world of possibilities for the blind 🌎🔊🖼️'", expanded=True):
        st.markdown(
                """
                Hear2See is a project that transforms images into meaningful sounds, empowering the visually impaired to understand their surroundings like never before."
        
                **How does it work?🤔**
        
                1. Hear2See is an innovative assistive technology project designed to empower blind individuals by providing them with a unique way to comprehend their surroundings through the sense of sound. 
                
                2. This system employs image recognition technology and audio synthesis to create a seamless connection between what is seen and what is heard.
                
                📸 **Image Capture or Upload:** Users can capture images in real-time using their smartphone's camera or upload existing photos from their personal collections.
        
                🌐 **Real-Time Feedback:** Users receive instant audio feedback, enabling them to navigate their surroundings more effectively, interact with their environment, and gain a deeper understanding of the world around them.
                
                🤖 AI Learning: The system continues to learn and adapt to the user's preferences and feedback, enhancing the overall experience over time.

                🌟 Empowerment: Hear2See is not just a tool; it's a bridge to independence and inclusivity for the visually impaired. It empowers them to make informed decisions, enjoy richer experiences, and engage more fully in their daily lives.

                Hear2See is breaking down barriers and promoting a world where everyone, regardless of their visual abilities, can experience the world with greater confidence and understanding. Join us on this incredible journey of sensory transformation! 🌎🔊🖼️ 

            """
            )
   
if selected == "Image Capture":
    #st.title(f"You have selected {selected}")
    st.header("📸 Image Capture")
    st.write("Capture the moment with real-time photos using your smartphone's camera.")
    image = st.camera_input("")

if selected == "Image Upload":
    #st.title(f"You have selected {selected}")
    st.header("📁 Image Upload‎")
    st.write("Select and share photos from your personal collection.")
    data = st.file_uploader("")
       
       
       
if selected == "Contact":
    st.title(f"You have selected {selected}")
    st.header(":mailbox: Get In Touch With Us!")


    contact_form = """
    <form action="https://formsubmit.co/go2rushil@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)










    
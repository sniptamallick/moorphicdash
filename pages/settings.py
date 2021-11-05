import streamlit as st


def app():
    st.write("Profile Settings")

    photo = st.file_uploader("Upload a Photo")

    firstname = st.text_input("First Name")

    lastname = st.text_input("Last Name")

    height =  st.text_input("Height")

    weight =  st.number_input("Weight")


    st.write("Daily Goals")

    distance =  st.number_input("Distance")

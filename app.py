import streamlit as st

st.title("PET CARE ASSISTANT")

st.header("Choose your pet:")

if st.button("🐶 Dog"):
    st.write("You selected Dog!")
    
if st.button("🐱 Cat"):
    st.write("You selected Cat!")

if st.button("🐦 Bird"):
    st.write("You selected Bird!")
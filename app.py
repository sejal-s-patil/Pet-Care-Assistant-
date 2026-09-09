import streamlit as st

st.title("PET CARE ASSISTANT")

st.header("Choose your pet:")

if st.button("🐶 Dog"):
    st.switch_page("pages/dog_breed.py")
    
if st.button("🐱 Cat"):
    
    st.switch_page("pages/cat_breed.py")

if st.button("🐦 Bird"):
    st.switch_page("pages/bird.py")
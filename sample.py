import streamlit as st
st.title("SivaKing2475")
st.write("Enter your Name :")
s=st.text_input("Enter your name :")
st.Button("Submit")
if s:
    st.write(s)

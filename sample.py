import streamlit as st
st.title("SivaKing2475")
st.sidebar.title("Give us your valid Info")
st.sidebar.text_input("Enter your Email ","Type here ...")
if st.sidebar.button("Submit"):
    st.sidebar.success("Your email verified")
st.text_input("Enter your name ","Type here ...")
st.date_input("Enter your DOB ")
st.text_input("Enter your Mobile Number","Type here ...")
st.radio("Select your Gender",["Male","Female","Others"])
if st.button("Submit"):
    st.write("Thank you for yor registration")
    st.success("Your Completed successfully")

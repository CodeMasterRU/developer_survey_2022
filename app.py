import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or predict", ("Predict", "Explore"))


if page == "Predict":
    show_predict_page()
else: 
    show_explore_page()

st.write("\n")
st.write("\n")
st.write("\n")

conclusion = "Made with 🤍"

st.markdown(f"<div align='center'>{conclusion}</div>", unsafe_allow_html=True)
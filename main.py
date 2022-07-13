import streamlit as st
import os

st.header("Hello EV World 3000")

funny_word = os.environ['TestSecret']
st.write(funny_word)

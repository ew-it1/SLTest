import streamlit as st
import os
#import sys


st.header("Hello EV World 3000")

#funny_word = os.environ['TestSecret']
#st.write(funny_word)

current_path = os.getcwd()

st.write(current_path)

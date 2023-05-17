import streamlit as st
import os
from supabase import create_client, Client
import pandas as pd
import numpy as np
#import sys


st.header("Hello EV World 3000")

#funny_word = os.environ['TestSecret']
#st.write(funny_word)

current_path = os.getcwd()

st.write(current_path)

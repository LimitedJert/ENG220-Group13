# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j4hn62Aa6yWS2DMrFSPjGkHzaljaE6N9
"""

import streamlit as st

# Your information
name = "Jerry Lu"
favorite_activity = "Games"
degree = "Computer Science"

# Title of the app
st.title("Welcome to My Streamlit App!")

# Display the information as a list
st.write("### About Me:")
st.write(f"- **Name**: {name}")
st.write(f"- **Favorite activity**: {favorite_activity}")
st.write(f"- **Degree**: {degree}")


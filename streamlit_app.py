import streamlit as st
from homepage import show_homepage
from result import show_result
from generateppt import show_ppt

st.set_page_config(page_title="Course Creator", page_icon="📚")

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

# Define page functions
pages = {
    "home": show_homepage,
    "result": show_result,
    "ppt": show_ppt
}

# Display the current page
pages[st.session_state.current_page]()
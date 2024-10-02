import streamlit_app as st
from homepage import show_homepage
from result import show_result
from generateppt import show_ppt
# import streamlit as st
# import google.generativeai as genai


st.set_page_config(page_title="Course Creator", page_icon="📚")

# Define pages
home_page = st.Page(show_homepage, title="Home", icon="🏠")
result_page = st.Page(show_result, title="Result", icon="📊")
ppt_page = st.Page(show_ppt, title="Generate PPT", icon="📝")

# Navigation
page = st.navigation([ home_page, result_page, ppt_page], position="hidden")

# Run the selected page
page.run()

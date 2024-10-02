

import streamlit as st
import google.generativeai as genai
from result import show_result


genai.configure(api_key='GOOGLE_GENAI_API_KEY')

def show_homepage():
    st.title("Course Creator")

    with st.form("course_form"):
        course_name = st.text_input("Enter your Course name")
        course_objective = st.text_area("Course Objective")
        age_group = st.selectbox("Select the age group", ["Children (5-12 years)", "Teens (13-18 years)", "Young Adults (19-25 years)", "Adults (26-40 years)", "Mature Learners (40+ years)"])
        skill_level = st.selectbox("Select the skill level of the audience", ["Beginner", "Intermediate", "Advanced"])
        language = st.selectbox("Select the primary language", ["Hindi", "Bengali", "Kannada", "Malayalam", "Marathi", "Odia", "Punjabi", "Tamil", "Telugu", "Gujarati"])
        tts_option = st.radio("Do you want Text-to-Speech for this language?", ("Yes", "No"))
        week_days = st.multiselect("Select the days of the week for the course", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        course_time = st.time_input("Select the course timing")
        prerequisite_subject = st.text_input("Enter prerequisite subject name")
        course_format = st.selectbox("Select course format", ["Online", "Offline", "Hybrid"])
        course_duration = st.number_input("Enter duration of the course (in months)", 0, 12)
        learning_outcomes = st.text_input("Enter learning outcomes")
        syllabus_file = st.file_uploader("Upload course syllabus or relevant PDF", type=["pdf", "docx"])
        generate_mcq = st.checkbox("Generate MCQs?")
        generate_question_bank = st.checkbox("Generate question bank?")
        generate_assignments = st.checkbox("Generate assignments?")
        generate_ppt = st.checkbox("Generate PPT?")

        submit_button = st.form_submit_button(label="Generate Course")

    if submit_button:
        course_data = f"""
        Course Name: {course_name}
        Course Objective: {course_objective}
        Target Audience: {age_group}, Skill Level: {skill_level}
        Language: {language} (Text-to-Speech: {tts_option})
        Schedule: Days - {', '.join(week_days)}, Time - {course_time}
        Prerequisite Subject: {prerequisite_subject}
        Course Format: {course_format}
        Duration: {course_duration} months
        Learning Outcomes: {learning_outcomes}
        Optional Features: 
            Generate MCQs: {generate_mcq}
            Generate Question Bank: {generate_question_bank}
            Generate Assignments: {generate_assignments}
            Generate PPT: {generate_ppt}
        """

        st.session_state.course_data = course_data
        st.session_state.generate_ppt = generate_ppt
        st.session_state.generate_mcq = generate_mcq
        st.session_state.generate_question_bank = generate_question_bank
        st.session_state.generate_assignments = generate_assignments
        st.session_state.language = language
        st.session_state.tts_option = tts_option
        result_page = st.Page(show_result, title="Result", icon="📊")
    
        page = st.navigation([ result_page], position="hidden")

        page.run()

        # st.switch_page("result")
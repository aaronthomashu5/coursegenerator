import streamlit as st
import google.generativeai as genai
import requests
import re
import base64
import json


GOOGLE_GENAI_API_KEY= st.secrets["GOOGLE_API_KEY"]
SARVAM_KEY = st.secrets["SARVAM_API_KEY"]
genai.configure(api_key=GOOGLE_GENAI_API_KEY)

# Sarvam API configuration
SARVAM_TRANSLATE_URL = "https://api.sarvam.ai/translate"
SARVAM_TTS_URL = "https://api.sarvam.ai/text-to-speech"


def generate_content(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-002')
    response = model.generate_content(prompt)
    return response.text

def translate_text(text, target_language_code):
    payload = {
        "input": text,
        "source_language_code": "en-IN",
        "target_language_code": target_language_code,
        "speaker_gender": "Male",
        "mode": "formal",
        "model": "mayura:v1",
        "enable_preprocessing": True
    }
    headers = {"Content-Type": "application/json", "api-subscription-key": SARVAM_KEY}
    response = requests.post(SARVAM_TRANSLATE_URL, json=payload, headers=headers)
    return response.text


def text_to_speech(text, target_language_code):
    output_file_path = "output_audio.mp3"
    payload = {
        "inputs": [text],
        "target_language_code": target_language_code,
        "speaker": "meera"
    }
    headers = {
        "api-subscription-key": SARVAM_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(SARVAM_TTS_URL, json=payload, headers=headers)

    try:
        audio_json = response.json()
        if "audio" in audio_json:
            audio_data_base64 = audio_json["audio"]
        elif "audios" in audio_json and len(audio_json["audios"]) > 0:
            audio_data_base64 = audio_json["audios"][0]
        else:
            raise KeyError("No audio data found in the response")
        
        audio_bytes = base64.b64decode(audio_data_base64)
        return audio_bytes
    except json.JSONDecodeError:
        print("Failed to decode JSON response")
        return None
    except KeyError as e:
        print(f"Key error: {str(e)}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def show_result():
    st.title("Course Result")


    if 'course_data' not in st.session_state:
        st.error("No course data found. Please go back to the home page and submit the form.")
        return

    st.write(st.session_state.course_data)
    course_data = st.session_state.course_data

    prompt = f"""
    Create a comprehensive course plan based on the following details:
    {course_data}
    give only the mentioned prompt's response. don't respond with messages which is not asked for eg"ppt generation is not possible"
    give response only for the input topic, dont respond out of topic if the input prompt isnt logical then dont mention it. 
    Provide the following:
    {"1. Full PowerPoint slides with Headlines and Short Body highlighting the keywords and necassary according to course details and pdf and covering all must learn topics with definition. minimum 10 slides" if st.session_state.generate_ppt else ""}
    2. A script for the course instructor to present about on each slide, script must be according to each slide, should have sentences of minimum 400 characters ended by period.
    3. Guidelines for the best course design and timeline
    {"4. A question bank" if st.session_state.generate_question_bank else ""}
    {"5. MCQs" if st.session_state.generate_mcq else ""}
    {"6. Assignments" if st.session_state.generate_assignments else ""}

PPT slides seperated by new line, output in mentioned language without markdown in this format:
Slide 1: Title: <content translated output or otherwise>
Body: <content translated output or otherwise>

Slide 2: Title: <content translated output or otherwise>
Body: <content translated output or otherwise>....
minimum slides 10
    Format the response as following only:
    (PPT)
    $$$
    (script)
    $$$
    (Guidelines)
    $$$
    (Question Bank)
    $$$
    (MCQs)
    $$$
    (Assignments)
    """

    with st.spinner("Generating course content..."):
        generated_content = generate_content(prompt)

    # Split the content
    content_parts = re.split(r'\$\$\$', generated_content)
    ppt_text_body, transcript_text_body, guideline, question_bank, mcqs, assignments = ("",) * 6

    if len(content_parts) >= 1 and st.session_state.generate_ppt:
        ppt_text_body = content_parts[0].strip()
    if len(content_parts) >= 2:
        transcript_text_body = content_parts[1].strip()
    if len(content_parts) >= 3:
        guideline = content_parts[2].strip()
    if len(content_parts) >= 4 and st.session_state.generate_question_bank:
        question_bank = content_parts[3].strip()
    if len(content_parts) >= 5 and st.session_state.generate_mcq:
        mcqs = content_parts[4].strip()
    if len(content_parts) >= 6 and st.session_state.generate_assignments:
        assignments = content_parts[5].strip()
    st.session_state.ppt_text_body = ppt_text_body
    print(ppt_text_body)
    st.session_state.transcript_text_body = transcript_text_body

    st.subheader("Please copy the generated Content and then Proceed with PPT")

    st.subheader("Course Transcript")
    st.write(transcript_text_body)

    st.subheader("Course Design Guidelines")
    st.write(guideline)

    if st.session_state.generate_question_bank:
        st.subheader("Question Bank")
        st.write(question_bank)

    if st.session_state.generate_mcq:
        st.subheader("MCQs")
        st.write(mcqs)

    if st.session_state.generate_assignments:
        st.subheader("Assignments")
        st.write(assignments)

    if st.button("Generate PPT"):

        st.session_state.current_page = "ppt"
        st.rerun()

    # Add other buttons for MCQ, question bank, and assignments if needed
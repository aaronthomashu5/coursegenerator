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

LANGUAGE_CODES = {
    "Hindi": "hi-IN",
    "Bengali": "bn-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Marathi": "mr-IN",
    "Odia": "od-IN",
    "Punjabi": "pa-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Gujarati": "gu-IN"
}

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
        "speaker": "arvind"
    }
    headers = {
        "api-subscription-key": SARVAM_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(SARVAM_TTS_URL, json=payload, headers=headers)
    audiotxt = response.text
    # print("API Response:", audiotxt)
    audio_json = json.loads(audiotxt)

    audio_data_base64 = audio_json["audios"][0]
    binary_data = base64.b64decode(audio_data_base64)
    with open(output_file_path, 'wb') as mp3_file:
        mp3_file.write(binary_data)
    # print(f"MP3 file saved successfully at {output_file_path}")

    return output_file_path

def show_result():
    st.title("Generated Course Content")

    if 'course_data' not in st.session_state:
        st.error("No course data found. Please go back to the home page and submit the form.")
        return

    course_data = st.session_state.course_data

    prompt = f"""
    Create a comprehensive course plan based on the following details:
    {course_data}
    give only the mentioned prompt's response. don't respond with messages which is not asked for eg"ppt generation is not possible"
    give response only for the input topic, dont respond out of topic if the input prompt isnt logical then dont mention it. 
    Provide the following:
    {"1. An outline for PowerPoint slides" if st.session_state.generate_ppt else ""}
    2. A transcript for the course instructor, this transcript helps instructor to give as an intro keep it simple keep it as short as possible
    3. Guidelines for the best course design and timeline
    {"4. A question bank" if st.session_state.generate_question_bank else ""}
    {"5. MCQs" if st.session_state.generate_mcq else ""}
    {"6. Assignments" if st.session_state.generate_assignments else ""}
    
    Format the response as follows:
    (PPT Outline)
    $$$
    (Transcript)
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

    if st.session_state.generate_ppt:
        if st.button("Generate PPT"):
            st.session_state.ppt_text_body = ppt_text_body
            # st.switch_page("generate_ppt")

    if st.session_state.tts_option == "Yes":
        target_language_code = LANGUAGE_CODES[st.session_state.language]
        with st.spinner("Translating and generating audio..."):
            translated_text = translate_text(transcript_text_body, target_language_code)
            audio_content = text_to_speech(transcript_text_body, target_language_code)
            
        st.subheader(f"Translated Transcript ({st.session_state.language})")
        # st.write(translated_text)
        
        st.subheader("Audio Version")
        st.audio(audio_content, format="audio/mp3")

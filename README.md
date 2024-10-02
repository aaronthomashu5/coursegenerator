# 📚 AI-Powered Course Creation Copilot 🚀

Welcome to the **AI-Powered Course Creation Copilot** repository! This project is a cutting-edge tool designed to assist educators in creating high-quality course content with ease and efficiency. By leveraging the power of Generative AI and integrating APIs like Gemini and Sarvam, the copilot simplifies the process of content generation, translation, and optimization, allowing instructors to focus on delivering effective learning experiences. 

---

## 🌟 Features

### 1. **Automated Course Content Generation** ✍️
- Generate comprehensive course materials including:
  - PowerPoint slides (PPT)
  - Instructor transcripts
  - Question banks 📝
  - Multiple-choice questions (MCQs)
  - Assignments 📚
  
### 2. **Translation & Text-to-Speech** 🌐
- Translate course content into multiple Indian languages using the **Sarvam API**.
- Enable **Text-to-Speech (TTS)** functionality for seamless auditory learning.

### 3. **Customizable Course Structure** ⚙️
- Tailor course design based on:
  - Audience (age group, skill level)
  - Language preferences
  - Course duration & schedule 📅
  - Format (online, offline, hybrid)

### 4. **Multi-format Content Output** 🖨️
- Generate course materials in:
  - PDF
  - PPT
  - Audio formats (MP3) 🎧

### 5. **Instructor Personalization & Flexibility** 🛠️
- Choose optional features like generating:
  - MCQs 🧠
  - Assignments
  - Question banks
- Personalize course flow and structure according to specific needs.

---

## 🏗️ Project Architecture

The solution is built on **Streamlit**, leveraging **Generative AI** through **Google’s Gemini API** and **Sarvam API** for translations and TTS capabilities.

- `app.py`: Main application file handling page routing and navigation.
- `homepage.py`: Form-based user input page for course creation.
- `result.py`: Displays generated content and manages translation and TTS functionalities.
- `generateppt.py`: Generates and handles PPT content output based on the selected course materials.

---

## 🔮 What's In-Scope?

1. **AI-Generated Course Content** 🧑‍🏫
   - Automatically generated PPT slides, instructor guides, assignments, and more.
   
2. **Translation & TTS** 🎙️
   - Translation into Indian languages like Hindi, Tamil, Bengali, and more.
   - Text-to-Speech for auditory learners.

3. **Custom Course Design** 🎓
   - Flexible structure and format for tailored learning experiences.

---

## 🚫 What's Out of Scope?

1. **Live Teaching/Management Tools**:
   - No real-time class management, student enrollment, or grading capabilities.
   
2. **Assessment Grading**:
   - Although the tool generates assessments, it does not automatically grade or analyze student performance.

---

## 🔮 Future Opportunities

1. **Personalized Learning** 🌱:
   - Tailor content dynamically based on student progress.

2. **LMS Integration**:
   - Seamless integration with popular Learning Management Systems for end-to-end course management.

3. **Gamification & Interactive Learning** 🎮:
   - Introduce gamified quizzes, interactive diagrams, and more to enhance engagement.

4. **Mobile & Cross-Platform Deployment** 📱:
   - Expand the copilot to mobile apps and browser extensions for on-the-go course creation.

---

## ⚡ Getting Started

### Prerequisites

1. **Python 3.9+** 🐍
2. **Streamlit**
   ```
   pip install streamlit
   ```
3. **Google Generative AI (Gemini) API** 🔑
   - Set up your API key [here](https://cloud.google.com/).
   
4. **Sarvam API** 🔑
   - Get your Sarvam API key [here](https://sarvam.ai/).

### Running the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/course-creation-copilot.git
   ```

2. Navigate into the project directory:
   ```bash
   cd course-creation-copilot
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🛠️ Contribution

We welcome contributions to make this project even better! 🎉 Feel free to:
- Open issues to report bugs or request features.
- Submit pull requests to contribute code or improve documentation.

---

## 🙌 Acknowledgments

- **Google Generative AI (Gemini)**
- **Sarvam API**
- **Streamlit** for the interactive frontend framework.

---

🚀 Happy teaching with **AI-Powered Course Creation Copilot**! Let's make education accessible, personalized, and efficient for everyone!
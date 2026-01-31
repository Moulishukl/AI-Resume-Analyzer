import streamlit as st
from resume_parser import extract_text
from skills import extract_skills
from login import login
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer & Career Recommendation System")

# Login Section
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.success("Login Successful!")
        else:
            st.error("Invalid Credentials")
    st.stop()

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

career_map = {
    "data analyst": ["python", "sql", "excel", "power bi"],
    "web developer": ["html", "css", "javascript", "react"],
    "machine learning engineer": ["python", "machine learning", "deep learning", "nlp"],
    "software developer": ["python", "java", "sql"]
}

if uploaded_file:
    text = extract_text(uploaded_file)
    found_skills, missing_skills = extract_skills(text)

    st.subheader("✅ Extracted Skills")
    st.write(found_skills)

    st.subheader("❌ Missing Skills")
    st.write(missing_skills)

    ats_score = min(len(found_skills) * 8, 100)
    st.subheader("📊 ATS Score")
    st.success(f"{ats_score}%")

    best_career = "General IT"
    for career, required_skills in career_map.items():
        match = len(set(found_skills) & set(required_skills))
        if match >= 2:
            best_career = career.title()

    st.subheader("🎯 Career Recommendation")
    st.info(best_career)

    st.subheader("🧠 AI Resume Feedback")
    if ats_score < 40:
        feedback = "Resume needs major improvement. Add more technical skills."
        st.error(feedback)
    elif ats_score < 70:
        feedback = "Resume is average. Improve projects and add more skills."
        st.warning(feedback)
    else:
        feedback = "Excellent resume! Ready for job applications."
        st.success(feedback)

    # Graph
    st.subheader("📈 Skill Strength Graph")
    if found_skills:
        plt.figure()
        plt.bar(found_skills, [1] * len(found_skills))
        plt.xticks(rotation=45)
        st.pyplot(plt)

    # Download Report
    report_text = f"""
Resume Analysis Report

Skills Found: {found_skills}
Missing Skills: {missing_skills}
ATS Score: {ats_score}%
Career Recommendation: {best_career}
Feedback: {feedback}
"""

    st.download_button("📄 Download Report", report_text, file_name="resume_report.txt")

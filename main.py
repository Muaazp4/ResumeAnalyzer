# main.py
import os
import spacy
import streamlit as st
from resume_extractor import extract_text_from_pdf, extract_text_from_txt
from skill_extractor import extract_skills
from match_job_description import calculate_match

# Install spaCy model if not already installed
if not spacy.util.is_package("en_core_web_sm"):
    os.system("python -m spacy download en_core_web_sm")

st.title("AI-Powered Resume Analyzer")

# Upload resume
uploaded_resume = st.file_uploader("Upload your Resume (PDF or TXT)", type=["pdf", "txt"])
if uploaded_resume:
    if uploaded_resume.name.endswith('.pdf'):
        resume_text = extract_text_from_pdf(uploaded_resume)
    else:
        resume_text = extract_text_from_txt(uploaded_resume)
    st.write("### Resume Content:")
    st.write(resume_text)

    # Extract skills
    skills = extract_skills(resume_text)
    st.write("### Extracted Skills:")
    st.write(", ".join(skills))

# Input job description
job_description = st.text_area("Paste Job Description (comma-separated skills)")
if job_description:
    match_percentage, matched_skills = calculate_match(skills, job_description)
    st.write(f"### Match Percentage: {match_percentage}%")
    st.write("### Matched Skills:")
    st.write(", ".join(matched_skills))

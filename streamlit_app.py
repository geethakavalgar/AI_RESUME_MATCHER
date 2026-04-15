import streamlit as st
from src.utils import extract_text
from src.model import get_similarity

st.title("AI Resume Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and job_desc:
        resume_text = extract_text(resume_file)
        score = get_similarity(resume_text, job_desc)
        st.success(f"Match Score: {score:.2f}")
    else:
        st.warning("Please upload a resume and enter job description")

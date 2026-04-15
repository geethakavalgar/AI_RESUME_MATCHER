# AI Resume Matcher Pro

An AI-powered application that compares a resume against a job description using semantic similarity and keyword overlap analysis.

## Features
- Upload a resume in PDF format
- Paste a job description
- Compute a semantic match score using Sentence Transformers
- Identify matched keywords and missing keywords
- Show top resume terms
- Interactive Streamlit UI for running and reviewing the analysis

## Tech Stack
- Python
- Streamlit (for building and executing the interactive app)
- Sentence Transformers
- scikit-learn
- PyMuPDF
- PyTorch / Torchvision

## Project Structure
```bash
ai_resume_matcher_pro/
├── streamlit_app.py
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── model.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## What It Demonstrates
- NLP-based resume analysis
- Embedding-based semantic similarity
- Keyword extraction and gap analysis
- User-facing AI application development with Streamlit

## Resume Bullet
Built an AI-powered resume matching application using Python, Sentence Transformers, scikit-learn, and Streamlit to compare resumes with job descriptions, generate semantic match scores, and identify missing skill keywords.

# Deployment Guide for Both Projects

## Option 1: Streamlit Community Cloud
Best for demos and portfolio visibility.

### Steps
1. Push each project to a separate GitHub repository.
2. Make sure each repo includes `requirements.txt` and the Streamlit app file.
3. Sign in to Streamlit Community Cloud.
4. Select **New app**.
5. Choose the repository and set the entry point to:
   - `app/streamlit_app.py`
6. Deploy.

### Notes
- Free and simple for portfolio use.
- Good for recruiter demos.
- Add screenshots to your README after deployment.

## Option 2: AWS EC2
Best if you want more control.

### High-level steps
1. Launch an Ubuntu EC2 instance.
2. Install Python and Git.
3. Clone the repository.
4. Create a virtual environment.
5. Install dependencies.
6. Run Streamlit:
   ```bash
   streamlit run app/streamlit_app.py --server.port 8501 --server.address 0.0.0.0
   ```
7. Open port 8501 in the security group, or place Nginx in front of it.

## Option 3: Docker
Add a `Dockerfile` and containerize either project for easier deployment.

### Sample Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Recommended Order
- Start with Streamlit Community Cloud for speed.
- Move to Docker or AWS once the repos are polished.

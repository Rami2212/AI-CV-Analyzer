import io
from openai import OpenAI
import streamlit as st
import PyPDF2
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI CV Analyzer", page_icon="🤖", layout="centered")

st.title("AI CV Analyzer")
st.markdown("Upload your CV and get insights powered by AI!")

uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you are applying for: (optional)")

analyze = st.button("Analyze CV")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

if analyze and uploaded_file:
    st.write("Analyzing your CV...")
    try:
        file_content = extract_text_from_file(uploaded_file)
        if not file_content.strip():
            st.error("The uploaded file is empty. Please upload a valid CV.")
            st.stop()
        st.write("CV content extracted successfully!")

        prompt = f"""Analyze the following CV and provide insights.
                    Focus on following aspects
                    1. Content clarity and aspects
                    2. Skills presentaion
                    3. Experience description
                    4. Specific improvements for {job_role if job_role else 'general job applications'}

                    CV Content:
                    {file_content}

                    Provide analysis in a clear and concise manner, highlighting strengths and areas for improvement."""

        client = OpenAI(
            api_key=os.getenv("AICC_API_KEY"),
            base_url=os.getenv("AICC_BASE_URL"),
        )

        if not os.getenv("AICC_API_KEY") or not os.getenv("AICC_BASE_URL"):
            st.error("API configuration missing. Please check environment variables.")
            st.stop()

        response = client.responses.create(
        model="gpt-5-mini",
        input=[
            {"role": "system", "content": "You are an expert CV analyzer providing actionable insights."},
            {"role": "user", "content": prompt},
        ],
        max_output_tokens=1000
        )

        st.markdown(response.output_text)


    except Exception as e:
        st.error(f"An error occurred while analyzing the CV: {str(e)}")

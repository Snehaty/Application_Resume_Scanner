import streamlit as st
from PyPDF2 import PdfReader

import io
import json
import base64
import google.generativeai as genai

genai.configure(api_key=st.secrets.GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
# Define cached functions
@st.cache_data()
def get_gemini_response(input, pdf_content, prompt):
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

@st.cache_data()
def get_gemini_response_keywords(input, pdf_content, prompt):
    response = model.generate_content([input, pdf_content[0], prompt])
    return json.loads(response.text[8:-4])


@st.cache_data()
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return [text]
    else:
        raise FileNotFoundError("No file uploaded")


# Streamlit App

st.set_page_config(page_title="ATS Resume Scanner")
st.header("Application Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if 'resume' not in st.session_state:
    st.session_state.resume = None

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    st.session_state.resume = uploaded_file

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    submit1 = st.button("Tell Me About the Resume")

with col2:
    submit2 = st.button("Get Keywords")

with col3:
    submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
 Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
As an expert ATS (Applicant Tracking System) scanner with an in-depth understanding of AI and ATS functionality, 
your task is to evaluate a resume against a provided job description. Please identify the specific skills and keywords 
necessary to maximize the impact of the resume and provide response in json format as {Technical Skills:[], Analytical Skills:[], Soft Skills:[]}.
Note: Please do not make up the answer only answer from job description provided"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response_keywords(input_prompt2, pdf_content, input_text)
        st.subheader("Skills are:")
        if response is not None:
            st.write(f"Technical Skills: {', '.join(response['Technical Skills'])}.")
            st.write(f"Analytical Skills: {', '.join(response['Analytical Skills'])}.")
            st.write(f"Soft Skills: {', '.join(response['Soft Skills'])}.")
    else:
        st.write("Please upload the resume")

elif submit3:
    if st.session_state.resume is not None:
        pdf_content = input_pdf_setup(st.session_state.resume)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
        st.markdown("---")
st.subheader("📝 Resume Summary Rewriter ")

with st.expander("💡 Improve your resume summary using AI"):
    resume_summary = st.text_area("📄 Paste your existing resume summary here:", height=150)

    if st.button("🔁 Rewrite Using Gemini"):
        if input_text.strip() == "":
            st.warning("⚠️ Please enter the Job Description above.")
        elif resume_summary.strip() == "":
            st.warning("⚠️ Please paste your current resume summary.")
        else:
            with st.spinner("Rewriting... please wait"):
                prompt = f"""
                You are an expert resume coach. Help improve the candidate's resume summary.

                Resume Summary:
                \"\"\"{resume_summary}\"\"\"

                Job Description:
                \"\"\"{input_text}\"\"\"

                Please rewrite the resume summary to better match the job description.
                Make it keyword-optimized, professional, and concise.
                """

                try:
                    response = model.generate_content(prompt)
                    st.success("✅ Rewritten Resume Summary:")
                    st.text_area("✍️ Improved Version", response.text.strip(), height=150)
                except Exception as e:
                    st.error(f"Error while rewriting: {e}")


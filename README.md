📄 ATS Resume Scanner (with AI)

A smart Streamlit-powered web app that simulates an Applicant Tracking System (ATS) — helping users evaluate how well their resume matches a given job description.

This tool uses AI (Google Gemini) to give human-like resume feedback, keyword suggestions, and matching percentage — making it ideal for jobseekers and career portals.
🚀 Features

    📄 Upload Resume: Upload your resume in PDF format.

    📝 Paste Job Description: Enter the job description directly in the app.

    🧠 “Tell Me About the Resume”: AI evaluates the resume, highlights strengths, weaknesses, and relevance.

    🔍 Extract Keywords: Uses NLP to extract important keywords and skills from JD.

    📊 Get Match Score: Calculates how well your resume matches the JD (%), missing keywords, and gives final thoughts.

    🖼 Resume Preview: Uses pdf2image to convert and show a preview of your resume.

🛠️ Technologies Used

    Python – Backend logic

    Streamlit – Web UI

    pdf2image – PDF to image conversion

    PyPDF2 – PDF parsing

    Google Gemini Pro API – To generate personalized AI feedback

    Regex + NLP – To extract relevant skills and keywords

⚙️ Installation
1. Clone the Repository

git clone https://github.com/Snehaty/Application_Resume_Scanner.git
cd Application_Resume_Scanner

2. Create & Activate a Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies

pip install -r requirements.txt

🔧 Setup for pdf2image (Poppler Requirement)

    Download from: https://github.com/oschwartz10612/poppler-windows/releases

    Extract it to:

C:\poppler

    Add this to your System PATH:

C:\poppler\Library\bin

✅ This is necessary for converting PDFs to images inside the app.
🔐 Set up Gemini API Key

    Create this file in your project:

.streamlit/secrets.toml

    Paste your key:

GOOGLE_API_KEY = "your-api-key-here"

▶️ Running the App

Make sure you're in the root directory:

streamlit run resume_tracker/app.py

Then open http://localhost:8501 in your browser.


💡 Use Cases

    For job seekers to tailor resumes to specific roles

    For career coaches or HR portals to give resume feedback

    For building a portfolio project with LLM + NLP integration

🌐 Deployment (Optional)

You can deploy this app for free using Streamlit Cloud.
Let me know if you'd like help deploying!
👩‍💻 Author

Sneha Tyagi
🔗 GitHub: @Snehaty
⭐️ Show Some Love

If you found this useful, give the repo a ⭐️ and share it!
Happy job hunting! 🚀💼

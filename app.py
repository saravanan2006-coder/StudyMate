import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# 1. Setup and Configuration
st.set_page_config(page_title="EC Prep", page_icon="📚")
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ API Key not found! Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# 2. UI Header
st.title("🎓 EC Prep")
st.info("Upload your notes to get started.")

# 3. File Upload Section
uploaded_file = st.file_uploader("Upload your PDF notes", type="pdf")

if uploaded_file is not None:
    try:
        # Extract text from PDF
        with st.spinner("Reading PDF..."):
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        st.success(f"Successfully loaded: {uploaded_file.name}")
        
        # 4. Action Buttons
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✨ Summarize Notes", use_container_width=True):
                with st.spinner("Generating Summary..."):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    prompt = f"""Role: Act as an expert academic tutor and subject matter specialist.
                            Task: Analyze the attached file thoroughly and provide a structured summary in a short way designed specifically for exam preparation and quick revision.
                            Requirements:
                            Core Summary: Provide a high-level overview (3-5 sentences) of the document's purpose and primary thesis.
                            Key Concepts & Definitions: Identify and define the most important technical terms, formulas, or theories mentioned. Use bold text for terms.
                            Thematic Breakdown (Key Points): Use bullet points to break the content into logical sections. Focus on 'The How' and 'The Why' rather than just 'The What.'   Exam Essentials: Highlight specific facts, dates, or mechanisms that are most likely to appear in a test environment.
                            Analogy/Simplification: Explain the most complex part of the file using a simple, real-world analogy to ensure conceptual clarity.
                            Practice Questions: Generate 3-5 short-answer questions based on the text to test my understanding.
                            Tone & Style: > * Use clear, professional, yet accessible language.
                            Avoid fluff or repetitive phrasing.
                            Use Markdown (headings, bolding, and lists) to make the response highly scannable.
                            Constraint: If the document contains diagrams or tables, summarize their data accurately within the relevant sections.: {text[:15000]}"""
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.subheader("📝 Key Study Points")
                    st.markdown(response.text)
                    
        with col2:
            if st.button("❓ Create Practice Quiz", use_container_width=True):
                with st.spinner("Creating Questions..."):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    prompt = f"Based on these notes, create a wise and important 10 Multiple Choice Questions (MCQs) for a exam. Include the correct answers at the very bottom: {text[:15000]}"
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.subheader("✍️ Practice Quiz")
                    st.markdown(response.text)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
        st.info("Tip: If you see a 'Not Found' error, check if your internet is connected or if the API key is correct.")

else:
    st.write("Please upload a PDF file to enable the study tools.")
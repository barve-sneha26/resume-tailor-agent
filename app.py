import streamlit as st
from tasks.jd_task import jd_task
from tasks.resume_task import resume_task
from tasks.tailoring_task import tailoring_task
from utils.extract_pdf import extract_resume_text
from utils.formatter import save_tailored_resume_md

st.set_page_config(page_title="Resume Tailoring Agent", layout="centered")
st.title("🧠 Resume Tailoring Agent")

# --- INPUTS ---
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description", height=250)

if uploaded_file and job_description:
    if st.button("Generate Tailored Suggestions"):
        with st.spinner("Analyzing..."):

            # Extract resume text
            resume_text = extract_resume_text(uploaded_file)

            # Run JD analysis
            jd_result = jd_task.invoke({"job_description": job_description}).content

            # Run resume analysis
            resume_result = resume_task.invoke({"resume_text": resume_text}).content

            # Generate tailored output
            tailored_output = tailoring_task.invoke({
                "jd_summary": jd_result,
                "resume_analysis": resume_result
            }).content

            # Save to markdown
            file_path = save_tailored_resume_md(tailored_output)
            st.success("✅ Tailored Resume Suggestions Ready!")

            # Display result
            st.subheader("💡 Tailored Suggestions")
            st.markdown(tailored_output)

            with open(file_path, "r") as f:
                st.download_button("📥 Download Markdown", f, file_name=file_path.split("/")[-1])

else:
    st.info("Please upload your resume and paste a job description to begin.")



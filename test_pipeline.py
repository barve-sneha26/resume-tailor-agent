from tasks.jd_task import jd_task
from tasks.resume_task import resume_task
from tasks.tailoring_task import tailoring_task
from utils.extract_pdf import extract_resume_text

from utils.formatter import save_tailored_resume_md 

# Load input files
job_description = """..."""
resume_text = extract_resume_text("data/sample_resume.pdf")

# Step 1: JD Analysis
jd_result = jd_task.invoke({"job_description": job_description}).content
print("\n=== JD ANALYSIS ===\n", jd_result)

# Step 2: Resume Analysis
resume_result = resume_task.invoke({"resume_text": resume_text}).content
print("\n=== RESUME ANALYSIS ===\n", resume_result)

# Step 3: Tailoring Output
tailored_output = tailoring_task.invoke({
    "jd_summary": jd_result,
    "resume_analysis": resume_result
}).content

print("\n=== TAILORED RESUME SUGGESTIONS ===\n", tailored_output)



# Save to Markdown file
output_path = save_tailored_resume_md(tailored_output)
print(f"\n✅ Tailored resume saved to: {output_path}")

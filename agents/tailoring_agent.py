from langchain_core.prompts import PromptTemplate
from agents.jd_agent import llm  # reuse same LLM

tailoring_prompt = PromptTemplate(
    input_variables=["jd_summary", "resume_analysis"],
    template="""
You are a resume improvement assistant.

Based on the following job description insights:
{jd_summary}

And the candidate's current resume analysis:
{resume_analysis}

Suggest how the resume can be rewritten to better match the job.
- Rewrite or add 2–3 bullet points that reflect JD priorities
- Make suggestions to improve alignment with skills/tone
- Be concise and ATS-friendly

Output should include improved bullet points and suggestions.
"""
)

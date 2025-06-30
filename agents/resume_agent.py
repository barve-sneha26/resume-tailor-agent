from langchain_core.prompts import PromptTemplate
from agents.jd_agent import llm  # reuse same LLM

resume_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
You are a resume analysis expert.

Analyze the following resume and extract:
1. Key technical skills
2. Work experience (summarized)
3. Education
4. Summary or personal branding statement (if any)

Respond in clearly labeled sections.

Resume Text:
{resume_text}
"""
)


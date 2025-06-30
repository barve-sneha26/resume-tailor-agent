from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

jd_prompt = PromptTemplate(
    input_variables=["job_description"],
    template="""
You are an expert HR analyst.

Analyze the following job description and extract the following:
1. Key technical skills
2. Key soft skills
3. Primary responsibilities
4. Desired tone or traits (e.g., fast-paced, detail-oriented)

Respond in clearly labeled sections.

Job Description:
{job_description}
"""
)

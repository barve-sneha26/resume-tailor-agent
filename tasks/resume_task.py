from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from agents.resume_agent import resume_prompt, llm

resume_task = resume_prompt | llm

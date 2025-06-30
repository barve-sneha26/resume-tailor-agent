from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from agents.jd_agent import jd_prompt, llm

jd_task = jd_prompt | llm

from langchain_core.runnables import RunnableLambda
from agents.tailoring_agent import tailoring_prompt, llm

tailoring_task = tailoring_prompt | llm

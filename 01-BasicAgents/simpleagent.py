from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

 
import os
from dotenv import load_dotenv
load_dotenv()
 
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
groq_model = os.getenv("GROQ_MODEL")
 
agent=Agent(
    model=Groq(id=groq_model),
    description="Yor are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True
)


                         
# response = agent.run("What is the capital of France?")
# print(response) 

agent.print_response("Which is the smallest country in the world?")
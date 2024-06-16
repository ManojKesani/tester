
from crewai import Agent, Task, Crew

from langchain_openai import ChatOpenAI

from llm_src import LLMClient

import os
from agents import AgentCreator

import PyPDF2
from textwrap import dedent


LLM = LLMClient()
a = AgentCreator('agents.json')

llm = LLM.get_llm(model_name='groq')

developer_agent = a.create_agent('Python developer',llm)
tester_agent = a.create_agent('Python tester',llm)

# Open the file in read mode
with open( './code1.py', 'r') as file:
    # Read the contents of the file
    code1 = file.read()

with open( './code2.py', 'r') as file:
    # Read the contents of the file
    code2 = file.read()


with open('./err.txt', 'r') as file:
    # Read the contents of the file
    err = file.read()



task = Task(
  description=dedent(f'''given the code 
                     -------------------code----------------------

                     {code1}

                     ---------------------------------------------


                     -------------------test code----------------------
                     {code2}
                     ---------------------------------------------

                     an the error 

                     -------------------error from the test ----------------------
                     {err}
                     
                     ---------------------------------------------

                    adapt the original code to resolve the issue
                         
                        '''),
  expected_output=dedent(f'''A well written python file with comments and mainly nothing else
'''),
  agent=developer_agent,
  output_file='code3.py'
)




crew = Crew(
            agents=[developer_agent],
            tasks=[task],
            verbose=2
        )

result = crew.kickoff()

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

tester_agent = a.create_agent('Python tester',llm)


task = Task(
   description=dedent(f'''
                    the task is to write a python code to check if its working properly and all lines are being converted,
                    save the errors into a error text file
                         
                        '''),
                        # there is a python code that reads a csv file with ID,first_name,last_name and combines the first and last name to a single Name and saves ID and Name to another csv.
  expected_output=dedent(f'''A well written python file with comments and mainly nothing else
'''),
  agent=tester_agent,
  output_file='code2.py'
)


crew = Crew(
            agents=[tester_agent],
            tasks=[task,],
            verbose=2
        )

result = crew.kickoff()

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



task = Task(
  description=dedent(f'''create a python code to read a csv file that has 3 rows, with col names ID, First_Name and Last_Name,
                     and combine the first_name and last_name to name and save a new csv file with id and name
                         
                        '''),
  expected_output=dedent(f'''A well written python file with comments and mainly nothing else
'''),
  agent=developer_agent,
  output_file='code1.py'
)


task2 = Task(
   description=dedent(f'''
                    the task is to take the input csv file and output csv file,
                    write a python code to do unit tests on them to check if it is working properly and converting all the rows.
                      use the code created by the previous task called code1.py to do the tests
                      
                    
                         
                        '''),
                        # there is a python code that reads a csv file with ID,first_name,last_name and combines the first and last name to a single Name and saves ID and Name to another csv.
  expected_output=dedent(f'''A well written python file with comments and mainly nothing else
'''),
  agent=tester_agent,
  output_file='code2.py'
)

task2.context = [task]

crew = Crew(
            agents=[developer_agent,tester_agent],
            tasks=[task,task2],
            verbose=2
        )

result = crew.kickoff()
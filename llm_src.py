# from langchain_openai import 
from langchain_community.chat_models import ChatOpenAI
# from langchain.llms import OpenAI

import os

from langchain.chat_models import ChatOpenAI as oai
from langchain_groq import ChatGroq


from dotenv import dotenv_values

# Load variables from .env file
env_vars = dotenv_values(".env")

# Access variables
for key, value in env_vars.items():
    os.environ[key] = value








class LLMClient:
    def __init__(self):

        self.model_dict = {'phi':"crew_phi3:latest",
                      'gemma':'crew_gemma:latest',
                      }
        self.base_url = "http://localhost:11434/v1"
        
    def get_llm(self,model_name):

        if model_name == 'phi':
            model = self.model_dict[model_name]

            llm = ChatOpenAI(
                model=model,
                base_url=self.base_url)
            return llm
        
        if model_name == 'gemma':
            model = self.model_dict[model_name]

            llm = ChatOpenAI(
                model=model,
                base_url=self.base_url)
            return llm
        
        if model_name == 'openai':
            return ChatOpenAI(model='gpt-3.5-turbo')
        
        if model_name == 'groq':
            print('creating groq llm')
            return ChatGroq(api_key='',
                            model='llama3-70b-8192',
                            temperature=0)


            

        
 
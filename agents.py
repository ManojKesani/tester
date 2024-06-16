import json
from crewai import Agent

class AgentCreator:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.json_file = json_file
            self.data = json.load(f)

    def create_agent(self, key,my_llm,max_iter=15,max_rpm=None,verbose=True,allow_delegation=False,cache=True,tools=[]):
        role = self.data['roles'].get(key)
        goal = self.data['goals'].get(key)
        backstory = self.data['backstories'].get(key)
        
        if role and goal and backstory:

            agent = Agent(
                    role=role,
                    goal=goal,
                    backstory=backstory,
                    tools=tools,  # Optional, defaults to an empty list
                    llm=my_llm,  # Optional
                    # function_calling_llm=my_llm,  # Optional
                    max_iter=max_iter,  # Optional
                    max_rpm=max_rpm, # Optional
                    verbose=verbose,  # Optional
                    allow_delegation=allow_delegation,  # Optional
                    # step_callback=my_intermediate_step_callback,  # Optional
                    cache=cache  # Optional
                    )



            return agent
        else:
            print("Role, goal, or backstory not found.")
            self.display_available_agents()
            return None

    def display_available_agents(self):
        print("Available Agents:")
        for key in self.data['roles']:
            print("- Key:", key)
            print("  Role:", self.data['roles'][key])
            print("  Goal:", self.data['goals'][key])
            print("  Backstory:", self.data['backstories'][key])
            # if 'tools' in self.data and key in self.data['tools']:
            #     print("  Tools:", ", ".join(self.data['tools'][key]))
            # else:
            #     print("  Tools: None")


    def add_agent(self, key, role, goal, backstory):
        if key not in self.data['roles']:
            self.data['roles'][key] = role
            self.data['goals'][key] = goal
            self.data['backstories'][key] = backstory
            print(f"Agent '{role}' added successfully.")
            self._save_json()
        else:
            print(f"Agent with key '{key}' already exists.")

    def _save_json(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)



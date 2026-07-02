from .client import ask_claude

def planner_agent(query):
    prompt = f'''
create a plan 
Query: 
{query}
'''
    return ask_claude(prompt) 
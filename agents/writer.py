from .client import ask_claude

def writer_agent(query,research):
    prompt = f'''
Query: 
{query} 


Research: 
{research}

write answer.
'''
    return ask_claude(prompt)
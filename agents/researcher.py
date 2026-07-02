from .client import ask_claude

def research_agent(query,plan):
    prompt = f'''
Query:{query}
plan:
{plan}
Research needed
'''
    return ask_claude(prompt) 
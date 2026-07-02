from .planner import planner_agent
from .researcher import research_agent
from .writer import writer_agent

async def execute(query):
    plan = planner_agent(query) 
    research = research_agent(
        query, 
        plan
    )
    answer = writer_agent(
        query, 
        research 
    )

    return answer 

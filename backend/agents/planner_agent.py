from crewai import Agent
from config.llm_config import llm

planner_agent = Agent(
    role="Planner",
    goal="Break down the research topic into 3 subtopics.",
    backstory="A brilliant academic expert known for research decomposition.",
    verbose=True,
    llm=llm
)
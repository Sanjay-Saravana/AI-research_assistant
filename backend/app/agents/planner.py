from crewai import Agent

planner_agent = Agent(
    role="Planner",
    goal="Break down a research topic into subtopics for exploration",
    backstory="You're a skilled academic who decomposes complex questions into manageable research queries.",
    verbose=True,
    allow_delegation=True
)
from crewai import Agent
from app.tools.search_tool import SearchTool

search_agent = Agent(
    role="Searcher",
    goal="Search recent research papers based on given subtopics",
    backstory="You are a research scientist who uses Semantic Scholar to locate relevant papers.",
    tools=[SearchTool()],
    verbose=True
)
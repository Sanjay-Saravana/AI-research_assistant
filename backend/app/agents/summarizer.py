from crewai import Agent
from app.tools.summarize_tool import SummarizeTool

summarizer_agent = Agent(
    role="Summarizer",
    goal="Summarize research abstracts into concise insights",
    backstory="You are an AI research assistant trained to extract key points from complex scientific text.",
    tools=[SummarizeTool()],
    verbose=True
)
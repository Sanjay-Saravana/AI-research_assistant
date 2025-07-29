from crewai import Agent
from tools.summarize_tool import SummarizeTool
from config.llm_config import llm

summarizer_agent = Agent(
    role="Summarizer",
    goal="Summarize the research papers and make them easy to understand.",
    backstory="A research assistant with a PhD in science communication.",
    tools=[SummarizeTool()],
    verbose=True,
    llm=llm
)
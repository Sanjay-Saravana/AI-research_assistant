from crewai import Agent
from config.llm_config import llm
from tools import SemanticScholarTool, ArxivTool, CrossrefTool, PDFExtractTool

search_agent = Agent(
    role="Searcher",
    goal="Collect full text of papers on each subtopic",
    backstory="You find the most relevant research and extract their full content for analysis.",
    verbose=True,
    llm=llm,
    tools=[ArxivTool(), CrossrefTool(), PDFExtractTool()],
    output_json=True
)
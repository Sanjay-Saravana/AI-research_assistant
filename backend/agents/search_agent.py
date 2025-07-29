from crewai import Agent
from tools.semantic_scholar import SemanticScholarTool
from tools.arxiv_tool import ArxivTool
from tools.crossref_tool import CrossRefTool
from config.llm_config import llm

search_agent = Agent(
    role="Searcher",
    goal="Find relevant papers and research material for the topic.",
    backstory="A digital librarian with access to multiple scientific databases.",
    tools=[SemanticScholarTool(), ArxivTool(), CrossRefTool()],
    verbose=True,
    llm=llm
)
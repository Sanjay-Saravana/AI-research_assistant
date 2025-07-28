from crewai_tools import BaseTool
import requests

class SemanticScholarTool(BaseTool):
    name = "Semantic Scholar Tool"
    description = "Search research papers using Semantic Scholar"

    def _run(self, query: str) -> str:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=3"
        response = requests.get(url)
        papers = response.json().get("data", [])
        return "\n\n".join(f"{p['title']} - {p.get('url', 'No URL')}" for p in papers)
from crewai.tools import BaseTool
import requests

class ArxivTool(BaseTool):
    name: str = "ArXiv Tool"
    description: str = "Search arXiv for research papers"

    def _run(self, query: str) -> str:
        url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=3"
        response = requests.get(url)
        # Simple parse of raw XML (can be improved with feedparser)
        entries = response.text.split("<entry>")
        results = []
        for entry in entries[1:]:
            title = entry.split("<title>")[1].split("</title>")[0].strip()
            link = entry.split("<id>")[1].split("</id>")[0].strip()
            results.append(f"{title} - {link}")
        return "\n\n".join(results)
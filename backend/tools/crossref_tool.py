from crewai.tools import BaseTool
import requests

class CrossRefTool(BaseTool):
    name: str = "CrossRef Tool"
    description: str = "Search scholarly metadata from CrossRef"

    def _run(self, query: str) -> str:
        url = f"https://api.crossref.org/works?query={query}&rows=3"
        response = requests.get(url)
        items = response.json().get('message', {}).get('items', [])
        return "\n\n".join(f"{item.get('title', [''])[0]} - {item.get('URL')}" for item in items)

if __name__ == "__main__":
    tool = CrossRefTool()
    query = "LLM"
    result = tool._run(query)
    print(result)
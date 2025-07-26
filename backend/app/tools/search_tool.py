from crewai import Tool
import requests
import xml.etree.ElementTree as ET

class SearchTool(Tool):
    name = "Multi-Source Paper Search Tool"
    description = "Search research papers from Semantic Scholar, arXiv, and CrossRef"

    def _run(self, query: str) -> str:
        result = "### 🔍 Search Results for: " + query + "\n\n"
        result += self._semantic_scholar(query)
        result += self._arxiv(query)
        result += self._crossref(query)
        return result

    def _semantic_scholar(self, query):
        try:
            url = "https://api.semanticscholar.org/graph/v1/paper/search"
            params = {"query": query, "limit": 2, "fields": "title,abstract,url"}
            res = requests.get(url, params=params).json()
            output = "\n📘 Semantic Scholar:\n"
            for paper in res.get("data", []):
                output += f"- **{paper['title']}**\n"
                output += f"  Abstract: {paper.get('abstract', 'N/A')}\n"
                output += f"  [Link]({paper['url']})\n\n"
            return output
        except Exception as e:
            return f"\nSemantic Scholar failed: {e}\n"

    def _arxiv(self, query):
        try:
            base_url = "http://export.arxiv.org/api/query"
            params = {"search_query": query, "start": 0, "max_results": 2}
            res = requests.get(base_url, params=params)
            root = ET.fromstring(res.text)
            output = "\n📗 arXiv:\n"
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
                link = entry.find('{http://www.w3.org/2005/Atom}id').text.strip()
                output += f"- **{title}**\n"
                output += f"  Abstract: {summary}\n"
                output += f"  [Link]({link})\n\n"
            return output
        except Exception as e:
            return f"\narXiv failed: {e}\n"

    def _crossref(self, query):
        try:
            url = "https://api.crossref.org/works"
            params = {"query": query, "rows": 2}
            res = requests.get(url, params=params).json()
            output = "\n📙 CrossRef:\n"
            for item in res.get("message", {}).get("items", []):
                title = item.get("title", ["No title"])[0]
                doi = item.get("DOI", "")
                link = f"https://doi.org/{doi}" if doi else "N/A"
                output += f"- **{title}**\n"
                output += f"  [DOI Link]({link})\n\n"
            return output
        except Exception as e:
            return f"\nCrossRef failed: {e}\n"
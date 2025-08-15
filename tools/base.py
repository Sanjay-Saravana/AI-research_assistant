from crewai.tools import BaseTool
import requests
from typing import List, Dict, Optional
from io import BytesIO
from PyPDF2 import PdfReader

class SemanticScholarTool(BaseTool):
    name: str = "Semantic Scholar Tool"
    description: str = "Searches for academic papers using Semantic Scholar"

    def _run(self, query: str) -> List[Dict[str, Optional[str]]]:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=2&fields=title,url,abstract,openAccessPdf"
        response = requests.get(url)
        data = response.json()
        results: List[Dict[str, Optional[str]]] = []
        for paper in data.get("data", []):
            results.append({
                "title": paper.get("title"),
                "url": paper.get("url"),
                "abstract": paper.get("abstract"),
                "pdf_url": paper.get("openAccessPdf", {}).get("url"),
                "source": "Semantic Scholar"
            })
        return results


class ArxivTool(BaseTool):
    name: str = "ArXiv Tool"
    description: str = "Searches for academic papers using ArXiv"

    def _run(self, query: str) -> List[Dict[str, str]]:
        url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=2"
        response = requests.get(url)
        results: List[Dict[str, str]] = []
        if response.status_code == 200:
            entries = response.text.split("<entry>")[1:]
            for entry in entries:
                title = entry.split("<title>")[1].split("</title>")[0].strip()
                link = entry.split("<id>")[1].split("</id>")[0].strip()
                results.append({
                    "title": title,
                    "url": link,
                    "pdf_url": link.replace("abs", "pdf") + ".pdf",
                    "source": "arXiv"
                })
        return results


class CrossrefTool(BaseTool):
    name: str = "CrossRef Tool"
    description: str = "Searches for academic papers using CrossRef"

    def _run(self, query: str) -> List[Dict[str, Optional[str]]]:
        url = f"https://api.crossref.org/works?query={query}&rows=2"
        response = requests.get(url)
        data = response.json()
        results: List[Dict[str, Optional[str]]] = []
        for item in data.get("message", {}).get("items", []):
            title = item.get("title", [""])[0]
            doi = item.get("DOI", "")
            pdf_url = f"https://doi.org/{doi}" if doi else None
            results.append({
                "title": title,
                "url": pdf_url,
                "pdf_url": pdf_url,
                "source": "CrossRef"
            })
        return results


class PDFExtractTool(BaseTool):
    name: str = "PDF Extract Tool"
    description: str = "Extracts and returns the full text from a given PDF URL"

    def _run(self, pdf_url: str) -> str:
        response = requests.get(pdf_url)
        if response.status_code == 200:
            try:
                reader = PdfReader(BytesIO(response.content))
                text: str = "\n".join([page.extract_text() or "" for page in reader.pages])
                return text[:5000]  # limit to 5000 characters
            except Exception as e:
                return f"Error extracting text: {e}"
        return "PDF could not be downloaded"
    
class SummarizerTool(BaseTool):
    name: str = "Summarizer Tool"
    description: str = "Summarizes the full text of papers into a concise summary"

    def _run(self, content: str) -> str:
        # Placeholder for actual summarization logic using an LLM
        if not content:
            return "No content provided."
        return f"Summary (preview): {content[:500]}..."
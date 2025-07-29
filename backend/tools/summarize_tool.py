from crewai.tools import BaseTool
import requests

class SummarizeTool(BaseTool):
    name: str = "Summarizer Tool"
    description: str = "Summarize content using local Ollama LLM"

    def _run(self, text: str) -> str:
        payload = {
            "model": "llama3",
            "prompt": f"Summarize the following content:\n\n{text}",
            "stream": False
        }
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        return response.json()['response']
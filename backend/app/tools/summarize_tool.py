from crewai import Tool
import openai
from app.core.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class SummarizeTool(Tool):
    name = "LLM Abstract Summarizer"
    description = "Summarizes paper abstracts into concise bullet points"

    def _run(self, text: str) -> str:
        prompt = f"Summarize the following scientific abstract in bullet points:\n\n{text}"
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Failed to summarize due to error: {e}"
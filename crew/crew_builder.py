from crewai import Crew, Task, Process
from agents.planner_agent import planner_agent
from agents.search_agent import search_agent
from agents.summarizer_agent import summarizer_agent

def run_research_pipeline(topic: str):
    # Task 1: Planning
    plan_task = Task(
        description=f"Break the topic '{topic}' into exactly 3 subtopics. Output as a JSON object like: {{ \"subtopics\": [\"...\"] }}",
        agent=planner_agent,
        expected_output="JSON object with a 'subtopics' key."
    )

    # Task 2: Searching using tool delegation
    search_task = Task(
        description="Use tools to search for papers on each subtopic and extract full content using PDFExtractTool.",
        agent=search_agent,
        expected_output="List of paper metadata (title, url, pdf_url, content) per subtopic.",
        depends_on=[plan_task]
    )

    # Task 3: Summarization
    summarize_task = Task(
        description="Use the collected full paper contents to create a summary report.",
        agent=summarizer_agent,
        expected_output="Final summary across all papers.",
        depends_on=[search_task]
        )

    crew = Crew(
        agents=[planner_agent, search_agent, summarizer_agent],
        tasks=[plan_task, search_task, summarize_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()
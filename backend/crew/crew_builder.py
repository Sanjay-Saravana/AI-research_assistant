from agents import planner_agent, search_agent, summarizer_agent
from crewai import Crew, Task, Process
from config.llm_config import llm

def run_research_pipeline(topic: str) -> str:
    plan_task = Task(
        description=f"Break the topic '{topic}' into 3 subtopics.",
        agent=planner_agent,
        expected_output="List of 3 subtopics"
    )

    search_task = Task(
        description="Search for papers on the subtopics.",
        agent=search_agent,
        depends_on=[plan_task]
    )

    summarize_task = Task(
        description="Summarize all collected papers into one cohesive summary.",
        agent=summarizer_agent,
        depends_on=[search_task]
    )

    crew = Crew(
        agents=[planner_agent, search_agent, summarizer_agent],
        model="ollama/llama3",
        tasks=[plan_task, search_task, summarize_task],
        cache=True,
        verbose=True,
        process=Process.sequential,
        planning=True,
        planning_llm=llm
    )

    return crew.run()
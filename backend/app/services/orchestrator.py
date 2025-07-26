from crewai import Crew
from app.agents import planner_agent, search_agent, summarizer_agent
from app.tasks import planner_task, search_task, summarize_task

def run_research(topic: str) -> str:
    # Define the sequence of tasks for the agents
    tasks = [
        planner_task(planner_agent, topic),
        search_task(search_agent),
        summarize_task(summarizer_agent),
    ]

    # Create a Crew with agents and tasks
    crew = Crew(
        agents=[planner_agent, search_agent, summarizer_agent],
        tasks=tasks,
        verbose=True  # Set False in production
    )

    # Run the crew and return final output
    result = crew.kickoff()
    return result

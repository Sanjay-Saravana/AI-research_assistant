from crewai import Task

def planner_task(agent, topic: str):
    return Task(
        description=f"""You are given a research topic: "{topic}".
        Break it down into specific and focused sub-questions that will guide a more detailed investigation.
        These sub-questions should be distinct, relevant, and researchable.""",
        expected_output="A numbered list of clear sub-questions.",
        agent=agent
    )

def search_task(agent):
    return Task(
        description="""Take the sub-questions provided by the Planner agent.
        For each sub-question, search research databases and return 2–3 relevant papers.
        For each paper, include:
        - Title
        - Abstract
        - Source (Semantic Scholar, arXiv, or CrossRef)
        - Link (if available)""",
        expected_output="List of papers with their titles, abstracts, and links grouped by sub-question.",
        agent=agent
    )

def summarize_task(agent):
    return Task(
        description="""Take the abstracts of the selected papers and summarize them.
        For each abstract, provide:
        - 3 bullet points summarizing the key findings or contributions
        - Keep each bullet under 25 words""",
        expected_output="Bullet-point summaries for each paper’s abstract.",
        agent=agent
    )
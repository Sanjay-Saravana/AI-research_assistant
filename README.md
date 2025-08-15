# Research AI – Powered by CrewAI, PyPDF2 & FastAPI

A research assistant API that automates extraction of insights from PDF documents using multi-agent collaboration (CrewAI), PDF handling (PyPDF2), and exposes results via a FastAPI interface.

---


## Overview

This project builds a **Research AI API** that searches for research paper and extract content, uses CrewAI agents to analyze and summarize content, and returns structured insights via FastAPI. The modular design enables tailored research workflows with minimal overhead.

---

## Features

- **AI Agent Crew** – Use CrewAI to orchestrate specialized agents (e.g., searcher, summarizer, topic analyzer, insight extractor).
- **Web API** – Expose endpoints (`/analyze`, `/status`, `/result`) using FastAPI.
- **Async Workflow** – Leverage asynchronous handling of file uploads, agent orchestration, and response streaming.
- **Structured Output** – Return results as JSON with clear summaries, topic tags, and extracted insights.

---

## Tech Stack

- **CrewAI** – for orchestrating autonomous multi-agent workflows :contentReference[oaicite:0]{index=0}  
- **PyPDF2** – for parsing and extracting text from PDF files  
- **FastAPI** – for building an asynchronous RESTful API  
- **Uvicorn / Gunicorn** – as ASGI server for deployment  
- **Optional**: `crewai-tools` suite for enhanced agent tools like web search or data context. :contentReference[oaicite:1]{index=1}  

---

## Getting Started

### Prerequisites

- Python ≥ 3.10 and < 3.14  
- A valid LLM API key (e.g., OpenAI) configured in `.env`

### Installation

```bash
git clone https://github.com/your-username/research-ai.git
cd research-ai

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt



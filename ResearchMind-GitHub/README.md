# ResearchMind — Multi-Agent AI Research System

ResearchMind is a Streamlit application that coordinates AI components to search the web, read a relevant webpage, draft a research report, and critique the report.

## Features

- Web search using Tavily
- Webpage text extraction using Requests and Beautiful Soup
- Research report generation using OpenAI's `gpt-4o-mini`
- Critic feedback with a score, strengths, and areas to improve
- Streamlit web interface and Markdown report download
- Command-line pipeline option

## Tech Stack

Python, Streamlit, LangChain, OpenAI API, Tavily Search API, Requests, Beautiful Soup

## Requirements

- Python 3.11 or 3.12 recommended
- Git (for version control)
- An OpenAI API key
- A Tavily API key

## Setup on Windows

Open PowerShell in the project folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, you can avoid changing execution policy and use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create a `.env` file in the project root using `.env.example` as a guide, then add your own keys:

```env
OPENAI_API_KEY=your_real_openai_api_key
TAVILY_API_KEY=your_real_tavily_api_key
```

Never commit `.env` or share API keys publicly. API usage may incur charges; check each provider's current pricing and limits.

## Run the web app

With the virtual environment activated:

```powershell
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`. Open it in your browser, enter a research topic, and run the research workflow.

## Run the command-line pipeline

```powershell
python pipeline.py
```

Enter a topic when prompted.

## Troubleshooting

- `streamlit is not recognized`: activate `.venv`, then run `python -m streamlit run app.py`.
- Missing API key: check that `.env` exists in the project root and that both key names are spelled correctly.
- Authentication, quota, or billing errors: verify your API keys and provider account limits.
- Dependency/import errors: confirm the virtual environment is active and reinstall with `python -m pip install -r requirements.txt`.
- Some websites block scraping; the Reader Agent may not be able to extract content from every URL.

## Project Structure

```text
ResearchMind/
├── app.py           # Streamlit interface
├── agents.py        # Search/reader agents and writer/critic chains
├── tools.py         # Tavily search and webpage scraping tools
├── pipeline.py      # Command-line research pipeline
├── requirements.txt
├── .env.example     # Environment variable template (no real secrets)
├── .gitignore
└── README.md
```

## How it works

1. Search Agent gathers relevant web results.
2. Reader Agent selects a relevant URL and extracts page text.
3. Writer generates a structured research report.
4. Critic evaluates the report and suggests improvements.

## License

Add a license only after confirming that you have permission to redistribute the original project's code and dependencies.

# 🔬 Research Agent AI — Multi-Agent Research System

An AI-powered research assistant that automates web research, extracts relevant information, synthesizes findings, and generates structured research reports using specialized AI agents.

Built with **Python, LangChain, Google Gemini, Tavily, and Streamlit**, this project demonstrates how multi-agent workflows can simplify information discovery and research report generation.

## ✨ Features

- **🔎 AI-Powered Web Search:** Retrieve relevant information from the web using Tavily Search API.
- **📄 Content Extraction:** Gather information from webpages for research and analysis.
- **🤖 Multi-Agent Workflow:** Use specialized agents for searching, reading, writing, and reviewing research.
- **📝 Automated Report Generation:** Synthesize collected information into structured research reports.
- **✅ AI Critic Agent:** Evaluate report quality, assign scores, and suggest improvements.
- **📚 Source References:** Include source URLs to help readers verify research findings.
- **🖥️ Interactive Web Interface:** Run research workflows through a Streamlit interface.
- **🐳 Docker Support:** Package the application into a portable container.
- **☁️ AWS Deployment:** Deploy the containerized application to a cloud server.

## 🏗️ System Architecture

```text
          User Research Query
                  |
                  v
        Streamlit Web Interface
                  |
                  v
       Multi-Agent Research Pipeline
                  |
          +-------+-------+
          |               |
          v               v
     Search Agent     Reader Agent
          |               |
          v               v
      Tavily API      Webpage Content
          |               |
          +-------+-------+
                  |
                  v
           Research Writer
                  |
                  v
            AI Critic Agent
                  |
                  v
       Structured Research Report
          + Sources & Findings
```

*Note: The architecture illustrates the intended workflow. Keep each component in the diagram only if it is implemented in your current codebase.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| LangChain | LLM integration and agent workflows |
| Google Gemini API | AI-powered reasoning and report generation |
| Tavily Search API | Web search and information discovery |
| Streamlit | Interactive web application |
| Docker | Containerization and deployment |
| AWS EC2 | Cloud hosting |

## 📁 Project Structure

```text
Research-Agent-AI/
├── app.py              # Streamlit application
├── agents.py           # AI agents and LLM configuration
├── pipeline.py         # Research workflow orchestration
├── tools.py            # Search and webpage tools
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image configuration
├── .dockerignore       # Excludes unnecessary build files
├── .gitignore          # Excludes sensitive and temporary files
├── .env.example        # Environment variable template
└── README.md           # Project documentation
```

*Adjust the file tree to match the actual files in your repository.*

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or newer, compatible with your dependencies
- Google Gemini API key
- Tavily API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/research-agent-ai.git
cd research-agent-ai
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the environment's Python executable directly instead.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get API credentials from:

- [Google AI Studio](https://aistudio.google.com/)
- [Tavily](https://tavily.com/)

**Security:** Never commit `.env` or expose API keys in source code, screenshots, logs, or public repositories.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL printed in the terminal, usually `http://localhost:8501`.

## 🐳 Run with Docker

Make sure Docker Desktop is installed and running.

### Build the image

```bash
docker build -t research-agent-ai:1.0 .
```

### Start the container

```bash
docker run -d --name research-agent-ai --env-file .env -p 8501:8501 research-agent-ai:1.0
```

Open [http://localhost:8501](http://localhost:8501).

### Useful Docker commands

```bash
docker ps
docker logs -f research-agent-ai
docker stop research-agent-ai
docker start research-agent-ai
```

## ☁️ AWS Deployment

The container can be deployed to an AWS EC2 instance.

High-level deployment workflow:

1. Launch an appropriate Ubuntu EC2 instance.
2. Configure SSH access and the application network port securely.
3. Install Docker and Git on the instance.
4. Clone the repository and configure API credentials securely.
5. Build the Docker image and start the container.
6. Access the application through the configured public endpoint.

For a public production deployment, configure HTTPS, restrict access where appropriate, and monitor AWS costs. Cloud hosting, public IP addresses, storage, and API usage may incur charges.

## 🔐 Security Best Practices

- Store API keys in environment variables rather than source code.
- Exclude `.env`, `.venv`, and temporary files from version control.
- Never bake API credentials into a Docker image.
- Restrict inbound network access and SSH permissions.
- Monitor Gemini and Tavily API quotas and usage.
- Use HTTPS and appropriate access controls for production deployments.

## 🚀 Future Improvements

- Add support for configurable research depth and output formats.
- Improve source verification and citation quality.
- Add research history and report export options.
- Introduce retries, rate-limit handling, and structured error reporting.
- Add automated tests and continuous integration.
- Improve deployment automation and production observability.

## 🎯 Project Objective

The goal of Research Agent AI is to demonstrate how specialized AI agents and web-search tools can work together to transform a user query into a structured, source-supported research report.

## 👨‍💻 Author

Keshav Kushwaha

- GitHub:https://github.com/keshavsingh70
- LinkedIn: https://www.linkedin.com/in/keshav-singh-kushwaha-785510193/

---

⭐ If you find this project interesting, consider giving the repository a star.

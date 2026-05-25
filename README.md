# Agentic RAG System with Multi-LLM Orchestration

An advanced, production-ready Retrieval-Augmented Generation (RAG) application built using **CrewAI** and **Streamlit**. The system intelligently parses, chunks, and searches through uploaded PDF documents using semantic analysis, falling back to live web search whenever document context is insufficient.

##  Live Application
🔗 **[https://agentic-rag-system-3gr6lrvk7qdrjmrihjmiks.streamlit.app](https://agentic-rag-system-3gr6lrvk7qdrjmrihjmiks.streamlit.app)**

---

## Key Technical Features
- **Multi-Model Orchestration:** Supports local and cloud deployment architectures utilizing **Llama 3.2** and **DeepSeek-R1** processors via Groq.
- **Agentic Workflow Architecture:** Powered by **CrewAI** agents configured with explicit search roles, goals, and backstories to maximize response accuracy.
- **Advanced Semantic Chunking:** Replaced standard token splitting with advanced semantic splitters (`Chonkie` & Microsoft's `MarkItDown`) to preserve structural meaning during text ingestion.
- **Cloud Vector Indexing:** Connects seamlessly to a high-performance **Qdrant Cloud** vector database cluster for fast, dense document retrieval.
- **Autonomous Web Fallback:** Integrated with a **Firecrawl** tool agent to scour live web indexes if the uploaded document lacks direct answers.

---

##  Technology Stack
- **Frontend / UI:** Streamlit Framework
- **Agentic Framework:** CrewAI, LangChain
- **Inference Engines:** Groq API (Llama 3.2 / DeepSeek-R1)
- **Vector Storage:** Qdrant Cloud DB
- **Document Processing:** MarkItDown, Chonkie Parsing Engine

---

## 📂 Repository Structure
```text
├── assets/                  # UI assets and logos
├── src/
│   └── agentic_rag/        # Core agent and tool logic
├── thumbnail/               # Media and documentation graphics
├── .gitignore               # Excludes environment files and system caches
├── README.md                # Main repository documentation
├── app_deep_seek.py         # App version configured for DeepSeek-R1
├── app_llama3.2.py          # Main deployment file utilizing Llama 3.2
└── requirements.txt         # Tailored, clean production dependencies

Local Execution Steps
Clone the Repository
Open your terminal or command prompt and clone this project repository to your local machine:

Bash

Bash
git clone [https://github.com/PreethiRagu/agentic-rag-system.git](https://github.com/PreethiRagu/agentic-rag-system.git)
cd agentic-rag-system
Set Up a Python Virtual Environment
Creating an isolated environment prevents module conflicts with other projects on your machine.

Bash

Bash
# Create the environment folder named '.venv'
python -m venv .venv

# Activate the environment:
# On Windows (Command Prompt / PowerShell):
.venv\Scripts\activate

# On macOS / Linux:
source .venv/bin/activate
Install Required Dependencies
Install the required packages from the project's dependency list:

Bash

Bash
pip install -r requirements.txt
Configure Local Environment Variables
Create a new file in the root folder of the project named exactly .env and add your secure cloud API infrastructure connections:

Code snippet

Code snippet
GROQ_API_KEY="your-groq-api-key-here"
QDRANT_URL="your-qdrant-cluster-url-here"
QDRANT_API_KEY="your-qdrant-api-key-here"
FIRECRAWL_API_KEY="your-firecrawl-api-key-here"
⚠️ Security Warning: Never commit your filled .env file to GitHub. The project's .gitignore file is configured to keep these keys private.

Boot up the Application Dashboard
Run the primary Streamlit service to open the interactive user interface in your web browser:

Bash

Bash
streamlit run app_llama3.2.py

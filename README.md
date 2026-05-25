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

---
##📦 Installation and Setup Guide

Follow these step-by-step instructions to configure environment keys, install the required dependencies, and run the Agentic RAG application locally on your machine.

---

## 🛠️ Prerequisites
Ensure you have **Python 3.10 or Python 3.11** installed on your system. You can verify this by opening your terminal or command prompt and running:
```bash
python --version


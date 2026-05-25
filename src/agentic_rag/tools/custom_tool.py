import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field, ConfigDict
from markitdown import MarkItDown
from chonkie import SemanticChunker
from qdrant_client import QdrantClient
from firecrawl import FirecrawlApp

# ==========================================
# ⚙️ HARDCODED CLOUD CREDENTIALS CONFIG
# ==========================================
# Paste your keys directly inside these quotation marks:
QDRANT_CLOUD_URL = "https://71b327a4-73ff-4a28-abe0-b38c2797956c.sa-east-1-0.aws.cloud.qdrant.io"
QDRANT_CLOUD_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6ZTQzMmI1ZDAtOGQxMC00NjY2LWI4YmUtZDFlNTY2MGFiMDUwIn0.F7CnnCNkzrv8GqXnDZyVQtJF9dPUT_mSxxlaR7J5HHw"

# ==========================================
# 1. LOCAL DOCUMENT SEARCH TOOL
# ==========================================
class DocumentSearchToolInput(BaseModel):
    """Input schema for DocumentSearchTool."""
    query: str = Field(..., description="Query to search the document.")

class DocumentSearchTool(BaseTool):
    name: str = "DocumentSearchTool"
    description: str = "Search the document for the given query."
    args_schema: Type[BaseModel] = DocumentSearchToolInput
    
    model_config = ConfigDict(extra="allow")
    
    def __init__(self, file_path: str):
        """Initialize the searcher with a PDF file path and set up the Qdrant Cloud connection."""
        super().__init__()
        self.file_path = file_path
        
        # Connects directly to your 24/7 Qdrant Cloud instances
        self.client = QdrantClient(
            url=QDRANT_CLOUD_URL,
            api_key=QDRANT_CLOUD_API_KEY
        )
        self._process_document()

    def _extract_text(self) -> str:
        """Extract raw text from PDF using MarkItDown."""
        md = MarkItDown()
        result = md.convert(self.file_path)
        return result.text_content

    def _create_chunks(self, raw_text: str) -> list:
        """Create semantic chunks from raw text."""
        chunker = SemanticChunker(
            embedding_model="minishlab/potion-base-8M",
            threshold=0.5,
            chunk_size=512,
            min_sentences=1
        )
        return chunker.chunk(raw_text)

    def _process_document(self):
        """Process the document and add chunks to Qdrant collection."""
        raw_text = self._extract_text()
        chunks = self._create_chunks(raw_text)
        
        docs = [chunk.text for chunk in chunks]
        metadata = [{"source": os.path.basename(self.file_path)} for _ in range(len(chunks))]
        ids = list(range(len(chunks)))

        self.client.add(
            collection_name="demo_collection",
            documents=docs,
            metadata=metadata,
            ids=ids
        )

    def _run(self, query: str) -> str:
        """Search the document with a query string."""
        relevant_chunks = self.client.query(
            collection_name="demo_collection",
            query_text=query
        )
        docs = [chunk.document for chunk in relevant_chunks]
        separator = "\n___\n"
        return separator.join(docs)


# ==========================================
# 2. FIRECRAWL WEB SEARCH FALLBACK TOOL
# ==========================================
class FirecrawlWebSearchToolInput(BaseModel):
    """Input schema for FirecrawlWebSearchTool."""
    query: str = Field(..., description="The search query to search the live web.")

class FirecrawlWebSearchTool(BaseTool):
    name: str = "FirecrawlWebSearchTool"
    description: str = "Search the web for real-time information when local documentation lacks answers."
    args_schema: Type[BaseModel] = FirecrawlWebSearchToolInput

    model_config = ConfigDict(extra="allow")

    def _run(self, query: str) -> str:
        """Execute a live search fallback using Firecrawl."""
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            return "Error: FIRECRAWL_API_KEY environment variable is missing."
            
        try:
            app = FirecrawlApp(api_key=api_key)
            search_result = app.search(query=query, params={"limit": 3})
            
            results = []
            for item in search_result.get("data", []):
                title = item.get("title", "No Title")
                snippet = item.get("description", item.get("markdown", ""))
                url = item.get("url", "")
                results.append(f"Title: {title}\nURL: {url}\nContent: {snippet}\n---")
                
            return "\n\n".join(results) if results else "No web results found."
        except Exception as e:
            return f"Failed web search routing: {str(e)}"
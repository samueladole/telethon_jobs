""""Factory for creating LLM clients based on configuration."""
from typing import Dict
from infrastructure.llm.ollama_client import OllamaClient
from infrastructure.llm.openai_client import OpenAIClient

def create_llm(config: Dict[str, str]):
    """Factory function to create LLM clients based on configuration."""
    if config["provider"] == "ollama":
        return OllamaClient(config["model"])
    if config["provider"] == "openai":
        return OpenAIClient(config["model"])
    raise ValueError("Unknown LLM provider")

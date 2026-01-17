import requests
from app.interfaces.llm_client import LLMClient


class OllamaClient(LLMClient):
    """A client for interacting with the Ollama LLM API."""

    def __init__(self, model: str = "llama3"):
        self.model = model

    def complete(self, prompt: str) -> str:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["response"]

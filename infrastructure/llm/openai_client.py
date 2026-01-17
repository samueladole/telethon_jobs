from openai import OpenAI
from app.interfaces.llm_client import LLMClient


class OpenAIClient(LLMClient):
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model

    def complete(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content

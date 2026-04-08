import httpx
from .config import settings


class OpenRouterClient:
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": settings.APP_URL,
            "X-Title": settings.PROJECT_NAME,
        }

    async def generate_completion(self, model: str, messages: list):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json={"model": model, "messages": messages},
            )
            response.raise_for_status()
            return response.json()


import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from the same folder
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

print("ENV FILE LOCATION:", env_path)
print("ENV FILE EXISTS:", env_path.exists())
print("NEWS KEY FOUND:", bool(os.getenv("NEWS_API_KEY")))

key = os.getenv("NEWS_API_KEY")


def news():
    if not key:
        print("News API key is missing.")
        return []

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "apiKey": key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("status") != "ok":
            print("News API Error:", data.get("message"))
            return []

        articles = data.get("articles", [])

        return [
            f"Number {i + 1}: {article['title']}"
            for i, article in enumerate(articles[:3])
            if article.get("title")
        ]

    except Exception as e:
        print("News Error:", e)
        return []

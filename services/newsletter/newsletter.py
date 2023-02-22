from typing import List
import requests
from app.config import NEWSLETTER_API_KEY, NEWSLETTER_API_ENDPOINT

def get_trending_newsletters(keyword: str) -> List[dict]:
    """
    Get trending newsletters based on a specific keyword
    """
    url = f"{NEWSLETTER_API_ENDPOINT}/newsletters?api_key={NEWSLETTER_API_KEY}&q={keyword}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        pass

def get_newsletter_content(newsletter_id: str) -> dict:
    """
    Get the content of a specific newsletter by ID
    """
    url = f"{NEWSLETTER_API_ENDPOINT}/newsletters/{newsletter_id}?api_key={NEWSLETTER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        pass

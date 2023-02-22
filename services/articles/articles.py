from typing import List

import requests
from requests.exceptions import RequestException


class ArticleService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_base_url = 'https://api.example.com/articles/'

    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Make a GET request to the API and return the response as a JSON object.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.get(self.api_base_url + endpoint, headers=headers, params=params)
            response.raise_for_status()
        except RequestException as e:
            print(f'Error making API request: {e}')
            return {}

        return response.json()

    def get_trending_articles(self, keyword: str) -> List[dict]:
        """
        Get a list of trending articles based on a specific keyword.
        """
        endpoint = 'trending'
        params = {
            'q': keyword
        }
        response_data = self._make_request(endpoint, params=params)

        articles = response_data.get('articles', [])
        return articles

    def refresh_token(self) -> bool:
        """
        Refresh the API token and update the class attribute.
        """
        endpoint = 'auth/refresh'
        response_data = self._make_request(endpoint)

        new_token = response_data.get('token')
        if new_token:
            self.api_key = new_token
            return True

        return False

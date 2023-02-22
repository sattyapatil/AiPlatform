import requests
import json
from config import RESEARCH_PAPER_API_KEY

class ResearchPaperService:
    """
    Service class to fetch research paper details from API
    """
    def __init__(self):
        self.api_key = RESEARCH_PAPER_API_KEY
        self.base_url = 'https://api.researchpapers.com/'

    def get_trending_papers(self, keyword):
        """
        Get trending research papers for given keyword

        :param keyword: str, keyword to search
        :return: list of dictionaries, research paper details
        """
        endpoint = f'{self.base_url}/papers?apikey={self.api_key}&q={keyword}&sort=views'
        response = requests.get(endpoint)

        if response.status_code == 200:
            return json.loads(response.text)['data']
        else:
            raise Exception("Failed to fetch research papers")

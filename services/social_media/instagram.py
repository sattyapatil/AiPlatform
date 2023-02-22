import requests


class InstagramService:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_trending_posts(self, keyword):
        url = f"https://api.instagram.com/v1/tags/{keyword}/media/recent?access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', [])
        else:
            raise Exception("Error fetching Instagram trending posts.")

    def refresh_access_token(self, client_id, client_secret, refresh_token):
        url = "https://api.instagram.com/oauth/access_token"
        payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get('access_token', None)
        else:
            raise Exception("Error refreshing Instagram access token.")

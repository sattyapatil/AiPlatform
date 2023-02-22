from linkedin_api import Linkedin
import time


class LinkedInService:

    def __init__(self, linkedin_credentials):
        self.linkedin_credentials = linkedin_credentials
        self.linkedin = None

    def get_linkedin_api(self):
        if not self.linkedin:
            self.linkedin = Linkedin(
                self.linkedin_credentials['email'],
                self.linkedin_credentials['password'],
                refresh_cookies=True
            )
        return self.linkedin

    def get_trending_posts(self, keyword):
        linkedin = self.get_linkedin_api()
        posts = []
        for i in range(1, 3):  # Get posts from first two pages
            results = linkedin.search(query=keyword, search_type='post', page=i)
            posts.extend(results.get('elements', []))
            time.sleep(1)  # Sleep to avoid hitting API rate limit
        return posts

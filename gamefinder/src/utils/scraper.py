import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, query):
        self.query = query
        self.results = []

    def fetch_results(self, num_pages=3):
        for page in range(num_pages):
            start = page * 10
            url = f"https://www.bing.com/search"
            params = {
                "q": self.query,
                "first": start,
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                self.results.extend(self.parse_results(response.text))
            else:
                print(f"Failed to retrieve results for page {page + 1}: {response.status_code} - {response.text}")

    def parse_results(self, html_data):
        soup = BeautifulSoup(html_data, 'html.parser')
        links = []
        for item in soup.find_all('li', {'class': 'b_algo'}):
            link = item.find('a')['href']
            if "education" not in link.lower():
                links.append(link)
        return links
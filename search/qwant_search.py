import requests
from bs4 import BeautifulSoup

def qwant_suche(query):
    url = f"https://www.qwant.com/?q={query.replace(' ', '+')}&t=web"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    ergebnisse = []
    for result in soup.select('a[data-testid="result-link"]'):
        titel = result.get_text(strip=True)
        link = result.get('href', '')
        if link.startswith('http'):
            ergebnisse.append({'titel': titel, 'link': link})
    return ergebnisse[:100]

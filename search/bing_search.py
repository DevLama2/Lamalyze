import requests
from bs4 import BeautifulSoup

def bing_suche(query):
    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    ergebnisse = []
    for result in soup.select('li.b_algo'):
        a = result.find('a')
        if a and a.get('href', '').startswith('http'):
            titel = a.get_text(strip=True)
            link = a['href']
            ergebnisse.append({'titel': titel, 'link': link})
    return ergebnisse[:100]

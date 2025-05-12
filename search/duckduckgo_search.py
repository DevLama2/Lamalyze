import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, parse_qs

def duckduckgo_suche(query):
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    ergebnisse = []
    for link in soup.select('.result__title a'):
        titel = link.get_text()
        raw_href = link.get('href')

        # DuckDuckGo leitet um – echte URL extrahieren
        if raw_href.startswith("/l/?kh="):
            parsed = urlparse(raw_href)
            ziel_url = parse_qs(parsed.query).get("uddg", [""])[0]
            ziel_url = unquote(ziel_url)  # URL-decoding
        else:
            ziel_url = raw_href

        if titel and ziel_url.startswith("http"):
            ergebnisse.append({'titel': titel, 'link': ziel_url})
    
    return ergebnisse[:5]

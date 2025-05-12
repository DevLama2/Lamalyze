import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def duckduckgo_suche(query):
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    ergebnisse = []
    for result in soup.select('.result'):
        link = result.select_one('.result__title a')
        if link:
            titel = link.get_text(strip=True)
            href = link.get('href', '')
            
            # Extract the actual URL from DuckDuckGo's redirect URL
            if '//duckduckgo.com/l/?uddg=' in href:
                href = href.split('uddg=')[1].split('&')[0]
                href = unquote(href)  # URL decode
                
            if href.startswith('http'):
                ergebnisse.append({'titel': titel, 'link': href})
    
    return ergebnisse[:100]

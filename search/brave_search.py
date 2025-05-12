import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def brave_suche(query):
    url = f"https://search.brave.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ergebnisse = []
    for result in soup.select('div.fdb'):
        title_element = result.select_one('a.h')
        if title_element:
            titel = title_element.get_text(strip=True)
            link = title_element.get('href', '')
            
            if link.startswith('http'):
                ergebnisse.append({"titel": titel, "link": link})

    return ergebnisse[:5]

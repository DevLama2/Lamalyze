import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def google_suche(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ergebnisse = []
    for result in soup.select('div.tF2Cxc'):
        title_element = result.select_one('h3.LC20lb')
        link_element = result.select_one('div.yuRUbf > a')
        
        if title_element and link_element:
            title = title_element.get_text(strip=True)
            link = link_element.get('href', '')
            
            if link.startswith('/url?q='):
                link = link.split('/url?q=')[1].split('&')[0]
                link = unquote(link)
            
            if link.startswith('http'):
                ergebnisse.append({"titel": title, "link": link})

    return ergebnisse[:5]

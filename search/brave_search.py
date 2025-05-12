import requests
from bs4 import BeautifulSoup

def brave_suche(query):
    url = f"https://search.brave.com/search?q={query.replace(' ', '+')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/90.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ergebnisse = []
    for eintrag in soup.select("div.snippet"):
        titel_tag = eintrag.find("a")
        if titel_tag:
            titel = titel_tag.get_text(strip=True)
            link = titel_tag["href"]
            if link.startswith("http"):
                ergebnisse.append({"titel": titel, "link": link})

    return ergebnisse[:5]

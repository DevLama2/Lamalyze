import requests
from bs4 import BeautifulSoup

def brave_suche(query):
    url = f"https://search.brave.com/search?q={query.replace(' ', '+')}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.93 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    

    soup = BeautifulSoup(response.text, "html.parser")
    ergebnisse = []

    # Robustere Suche nach Ergebnissen
    for eintrag in soup.select("div.snippet, div#results > div > div > div > div > div > div > div > div > a"):
        link_tag = eintrag.find("a")
        if not link_tag and eintrag.name == "a":
            link_tag = eintrag
        if link_tag and link_tag.get("href", "").startswith("http"):
            titel = link_tag.get_text(strip=True)
            link = link_tag["href"]
            ergebnisse.append({"titel": titel, "link": link})
    
    return ergebnisse[:5]

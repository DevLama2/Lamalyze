from flask import Flask, request, render_template
from search.duckduckgo_search import duckduckgo_suche
from search.bing_search import bing_suche
from search.qwant_search import qwant_suche
from search.brave_search import brave_suche
from search.google_search import google_suche

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ergebnisse = []
    search_engines = ["DuckDuckGo", "Brave", "Bing", "Qwant", "Google"]

    if request.method == "POST":
        suchbegriff = request.form.get("suchbegriff")
        if suchbegriff:
            
            # DuckDuckGo Suche
            try:
                duck_results = duckduckgo_suche(suchbegriff)
                ergebnisse.append(duck_results)
                print(f"DuckDuckGo Ergebnisse gefunden: {len(duck_results)}")
            except Exception as e:
                print(f"Fehler bei DuckDuckGo Suche: {str(e)}")
                ergebnisse.append([])
            # Brave Suche
            try:
                brave_results = brave_suche(suchbegriff)
                ergebnisse.append(brave_results)
                print(f"Brave Ergebnisse gefunden: {len(brave_results)}")
            except Exception as e:
                print(f"Fehler bei Brave Suche: {str(e)}")
                ergebnisse.append([])
            # Bing Suche
            try:
                bing_results = bing_suche(suchbegriff)
                ergebnisse.append(bing_results)
                print(f"Bing Ergebnisse gefunden: {len(bing_results)}")
            except Exception as e:
                print(f"Fehler bei Bing Suche: {str(e)}")
                ergebnisse.append([])

            # Qwant Suche
            try:
                qwant_results = qwant_suche(suchbegriff)
                ergebnisse.append(qwant_results)
                print(f"Qwant Ergebnisse gefunden: {len(qwant_results)}")
            except Exception as e:
                print(f"Fehler bei Qwant Suche: {str(e)}")
                ergebnisse.append([])

            # Google Suche
            try:
                google_results = google_suche(suchbegriff)
                ergebnisse.append(google_results)
                print(f"Google Ergebnisse gefunden: {len(google_results)}")
            except Exception as e:
                print(f"Fehler bei Google Suche: {str(e)}")
                ergebnisse.append([])
    
    
    return render_template("index.html", 
                         ergebnisse=ergebnisse, 
                         search_engines=search_engines,
                         request=request)

if __name__ == "__main__":
    app.run(debug=True)

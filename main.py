from flask import Flask, request, render_template
from search.duckduckgo_search import duckduckgo_suche
from search.brave_search import brave_suche
from search.google_search import google_suche

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ergebnisse = []
    search_engines = ["Google", "Brave", "DuckDuckGo"]
    if request.method == "POST":
        suchbegriff = request.form.get("suchbegriff")
        if suchbegriff:
            ergebnisse.append(google_suche(suchbegriff))
            ergebnisse.append(brave_suche(suchbegriff))
            ergebnisse.append(duckduckgo_suche(suchbegriff))
    
    return render_template("index.html", 
                         ergebnisse=ergebnisse, 
                         search_engines=search_engines,
                         request=request)

if __name__ == "__main__":
    app.run(debug=True)

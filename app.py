import os
from flask import Flask, jsonify
from supabase import create_client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet au frontend d'appeler l'API

# Récupération des variables d'environnement (configurées plus tard dans Render)
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def home():
    return {"message": "API Open Seat In Gabon - Bienvenue"}

@app.route('/api/offres')
def get_offres():
    """Renvoie la liste de toutes les offres d'emploi"""
    try:
        result = supabase.table("offres").select("*").execute()
        return jsonify(result.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/offres/recentes')
def get_recentes():
    """Renvoie les 10 dernières offres"""
    try:
        result = supabase.table("offres").select("*").order("id", desc=True).limit(10).execute()
        return jsonify(result.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

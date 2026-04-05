import os
from supabase import create_client

# Récupération automatique des secrets GitHub (variables d'environnement)
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase = create_client(url, key)

# Offres test (à remplacer plus tard par du vrai scraping)
offres = [
    {"titre": "Infirmier à Libreville", "entreprise": "Hôpital A", "lieu": "Libreville"},
    {"titre": "Vendeur en ligne", "entreprise": "Shop Gabon", "lieu": "Port-Gentil"},
    {"titre": "Développeur Web", "entreprise": "Startup Gabon", "lieu": "Libreville"}
]

for offre in offres:
    try:
        result = supabase.table("offres").insert(offre).execute()
        print(f"✅ Ajouté : {offre['titre']}")
    except Exception as e:
        print(f"❌ Erreur : {e}")

print("🎯 Script terminé !")

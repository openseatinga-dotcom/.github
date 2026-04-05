import os
from supabase import create_client

# Connexion à Supabase (les secrets GitHub seront utilisés automatiquement)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("❌ Erreur : Les variables SUPABASE_URL et SUPABASE_KEY ne sont pas définies")
    print("Vérifie que les secrets GitHub sont correctement configurés")
    exit(1)

supabase = create_client(url, key)

# Offres test (à remplacer plus tard par du vrai scraping)
offres_test = [
    {"titre": "Infirmier à Libreville", "entreprise": "Hôpital A", "lieu": "Libreville"},
    {"titre": "Vendeur en ligne", "entreprise": "Shop Gabon", "lieu": "Port-Gentil"},
    {"titre": "Développeur Web", "entreprise": "Startup Gabon", "lieu": "Libreville"}
]

print("🚀 Début de l'ajout des offres test...")
print(f"📡 Connexion à Supabase : {url}")

for offre in offres_test:
    try:
        result = supabase.table("offres").insert(offre).execute()
        print(f"✅ Ajouté : {offre['titre']} - {offre['entreprise']}")
    except Exception as e:
        print(f"❌ Erreur pour {offre['titre']} : {e}")

print("🎯 Script terminé !")

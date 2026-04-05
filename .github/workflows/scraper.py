import os
from supabase import create_client

# Connexion à Supabase (les secrets seront utilisés automatiquement)
url = os.environ["SUPABASE_URL"]
key = os.environ["SUPABASE_KEY"]

supabase = create_client(url, key)

# Exemple d'offres pour tester
offres_test = [
    {"titre": "Infirmier à Libreville", "entreprise": "Hôpital A", "lieu": "Libreville"},
    {"titre": "Vendeur en ligne", "entreprise": "Shop Gabon", "lieu": "Port-Gentil"},
    {"titre": "Développeur Web", "entreprise": "Startup Gabon", "lieu": "Libreville"}
]

print("🚀 Début de l'ajout des offres test...")

for offre in offres_test:
    try:
        result = supabase.table("offres").insert(offre).execute()
        print(f"✅ Ajouté : {offre['titre']}")
    except Exception as e:
        print(f"❌ Erreur pour {offre['titre']} : {e}")

print("🎯 Script terminé !")

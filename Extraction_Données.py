import pandas as pd
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('banque.db')

# Exécuter la requête SQL pour extraire les données des transactions
query = """
-- Ta requête SQL préparée ici
"""
data = pd.read_sql_query(query, conn)

# Fermer la connexion
conn.close()

print(data.head())

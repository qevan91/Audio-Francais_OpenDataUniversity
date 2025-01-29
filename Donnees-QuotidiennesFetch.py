import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('data/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv', encoding='ISO-8859-1', delimiter=';')

data.columns = ['Date', 'Chaine', 'N/A', 'Categorie', 'Nb_Sujets', 'Duree']
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
data['Annee'] = data['Date'].dt.year
data_cleaned = data.dropna(subset=['Categorie', 'Duree'])
data_2000 = data_cleaned[data_cleaned['Annee'] == 2000]
data_2020 = data_cleaned[data_cleaned['Annee'] == 2020]

def plot_pie_chart(data, year, ax):
    data_by_categorie = data.groupby('Categorie')['Nb_Sujets'].sum().reset_index()
    ax.set_title(f"Répartition des catégories en {year}")
    ax.pie(x=data_by_categorie['Nb_Sujets'], labels=data_by_categorie['Categorie'], autopct='%.2f%%')
    ax.axis('equal')

fig, axes = plt.subplots(1, 2, figsize=(18, 6))

plot_pie_chart(data_2000, 2000, axes[0])
plot_pie_chart(data_2020, 2020, axes[1])

plt.tight_layout()
plt.savefig('graphe/repartition_categories_2000_2010_2020.png')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv', encoding='ISO-8859-1', delimiter=';')

data.columns = ['Date', 'Chaine', 'N/A', 'Categorie', 'Nb_Sujets', 'Duree']
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
data['Annee'] = data['Date'].dt.year
data_cleaned = data.dropna(subset=['Categorie', 'Duree'])

data_2010 = data_cleaned[data_cleaned['Annee'] == 2010]
data_2019 = data_cleaned[data_cleaned['Annee'] == 2019]

def plot_pie_chart(data, year, ax):
    data_by_categorie = data.groupby('Categorie')['Nb_Sujets'].sum().reset_index()
    ax.set_title(f"Répartition des catégories en {year}")
    ax.pie(x=data_by_categorie['Nb_Sujets'], labels=data_by_categorie['Categorie'], autopct='%.2f%%')
    ax.axis('equal')

fig, axes = plt.subplots(1, 2, figsize=(18, 6))
plot_pie_chart(data_2010, 2010, axes[0])
plot_pie_chart(data_2019, 2019, axes[1])
plt.tight_layout()
plt.savefig('graphe/repartition_categories_2010_2019.png')
plt.show()

data_sport = data_cleaned[data_cleaned['Categorie'] == 'Sport']
data_sport_years = data_sport.groupby('Annee')['Nb_Sujets'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(data_sport_years['Annee'], data_sport_years['Nb_Sujets'], color='blue')
plt.title('Nombre de sujets sur le Sport par année')
plt.xlabel('Année')
plt.ylabel('Nombre de Sujets')
plt.xticks(data_sport_years['Annee'])
plt.savefig('graphe/sport_par_annee.png')
plt.show()

data_sante = data_cleaned[data_cleaned['Categorie'] == 'Santé']
data_sante_years = data_sante.groupby('Annee')['Nb_Sujets'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(data_sante_years['Annee'], data_sante_years['Nb_Sujets'], color='green')
plt.title('Nombre de sujets sur la Santé par année')
plt.xlabel('Année')
plt.ylabel('Nombre de Sujets')
plt.xticks(data_sante_years['Annee'])
plt.savefig('graphe/sante_par_annee.png')
plt.show()
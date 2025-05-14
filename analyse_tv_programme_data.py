import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv('data/ina-barometre-jt-tv-donnees-quotidiennes-2000-2020-nbre-sujets-durees-202410.csv',
                       encoding='ISO-8859-1', delimiter=';')
    data.columns = ['Date', 'Chaine', 'N/A', 'Categorie', 'Nb_Sujets', 'Duree']
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y', errors='coerce')
    data['Annee'] = data['Date'].dt.year
    return data.dropna(subset=['Categorie', 'Duree'])

def plot_pie_chart_by_year(data, year):
    data_year = data[data['Annee'] == year]
    data_grouped = data_year.groupby('Categorie')['Nb_Sujets'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(f"Répartition des catégories en {year}")
    ax.pie(x=data_grouped['Nb_Sujets'], labels=data_grouped['Categorie'], autopct='%.2f%%')
    ax.axis('equal')
    plt.tight_layout()
    return fig

def plot_bar_chart_by_category(data, selected_category):
    data_category = data[data['Categorie'] == selected_category]
    grouped = data_category.groupby('Annee')['Nb_Sujets'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(grouped['Annee'], grouped['Nb_Sujets'], color='skyblue')
    ax.set_title(f"Nombre de sujets sur « {selected_category} » par année")
    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre de Sujets")
    ax.set_xticks(grouped['Annee'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

import streamlit as st
from niveau_interet_information_par_groupe_sociaux import load_interest_data, plot_interest_levels
from analyse_tv_programme_data import load_data as load_tv_data, plot_pie_chart_by_year, plot_bar_chart_by_category

@st.cache_data
def loadInterestData():
    return load_interest_data()

@st.cache_data
def loadCategorieData():
    return load_tv_data()

InterestData = loadInterestData()
CategorieData = loadCategorieData()

st.title("📂 Dashboard Open Data University Les Françaises et Français et l'audiovisuel")

st.header("📈 L'intérêt des français à l'information")

all_groups = ["Employés", "Chomeur", "Chomeur à la recherche", "Étudiants", "Personne au foyer", "Retraités", "Inactif", "Ne souhaite pas répondre"]
selected_groups = st.multiselect("Choisissez les groupes sociaux à comparer :", all_groups, default=all_groups)

if selected_groups:
    fig = plot_interest_levels(InterestData, selected_groups)
    st.pyplot(fig)
else:
    st.warning("Veuillez sélectionner au moins un groupe pour afficher le graphique.")

st.header("📈 Comparaison du temps de parole des hommes et des femmes à la radio en 2019 et 2020")
st.image("graphe/Temps_Parole_Homme_Femme_Radio_19-20.png", caption="Comparaison du temps de parole des hommes et des femmes à la radio en 2019 et 2020")

st.header("📈 Comparaison du temps de parole des hommes et des femmes à la télévision en 2019 et 2020")
st.image("graphe/Temps_Parole_Homme_Femme_TV_19-20.png", caption="Comparaison du temps de parole des hommes et des femmes à la télévision en 2019 et 2020")

st.header("📈 Comparaison du temps de parole des hommes et des femmes à la télévision en 2019")
st.image("graphe/Temps_Parole_Femmes_Programmes_2019.png", caption="Temps de parole des femmes à la télévision en 2019")
st.image("graphe/Temps_Parole_Hommes_Programmes_2019.png", caption="Temps de parole des hommes à la télévision en 2019")

st.header("📈 Comparaison du temps de parole des hommes et des femmes à la télévision en 2020")
st.image("graphe/Temps_Parole_Femmes_Programmes_2020.png", caption="Temps de parole des femmes à la télévision en 2020")
st.image("graphe/Temps_Parole_Hommes_Programmes_2020.png", caption="Temps de parole des hommes à la télévision en 2020")

st.header("📊 Répartition des sujets par catégorie et par année")

available_years = sorted(CategorieData['Annee'].dropna().unique())
year1 = st.selectbox("Sélectionnez la première année :", available_years, index=available_years.index(2010) if 2010 in available_years else 0)
year2 = st.selectbox("Sélectionnez la deuxième année :", available_years, index=available_years.index(2019) if 2019 in available_years else 0)

col1, col2 = st.columns(2)
with col1:
    st.pyplot(plot_pie_chart_by_year(CategorieData, year1))
with col2:
    st.pyplot(plot_pie_chart_by_year(CategorieData, year2))

st.header("📈 Évolution du nombre de sujets par catégorie")

categories = sorted(CategorieData['Categorie'].unique())
selected_category = st.selectbox("Choisissez une catégorie :", categories, index=categories.index("Santé") if "Santé" in categories else 0)

st.pyplot(plot_bar_chart_by_category(CategorieData, selected_category))

import streamlit as st

st.title("📂 Dashboard Open Data University Les Françaises et Français et l'audiovisuel")

st.header("Répartition des thématiques")
st.image("graphe/repartition_categories_2010_2019.png", caption="Répartition des thématiques de 2010 à 2019")

st.header("Nombre de sujets sur la santé")
st.image("graphe/sante_par_annee.png", caption="Évolution du nombre de sujets sur la santé par année")

st.header("Nombre de sujets sur le sport")
st.image("graphe/sport_par_annee.png", caption="Évolution du nombre de sujets sur le sport par année")

st.header("L'intérêt des français à l'information")
st.image("graphe/interet_combined.png", caption="L'intérêt des français à l'information au fil du temps")
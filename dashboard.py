import streamlit as st

st.title("📂 Dashboard test")

repartition = "graphe/repartition_categories_2010_2019.png"
sante = "graphe/sante_par_annee.png"
sport = "graphe/sport_par_annee.png"

st.image(repartition, caption='Voici une image')
st.image(sante, caption='Voici une image')
st.image(sport, caption='Voici une image')
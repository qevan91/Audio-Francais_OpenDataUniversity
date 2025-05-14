import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_excel("data/les-francais-et-l-information-arcom-2024-base-anonymisee.xlsx", engine="openpyxl")

def plot_interest_levels(data, selected_groups):
    group_ids = {
        "Employés": 1,
        "Chomeur": 2,
        "Chomeur à la recherche": 3,
        "Étudiants": 4,
        "Personne au foyer": 5,
        "Retraités": 6,
        "Inactif": 7,
        "Ne souhaite pas répondre": 8
    }

    results = pd.DataFrame()

    for group_name in selected_groups:
        group_value = group_ids[group_name]
        group_data = data[data["RS3_R"] == group_value]
        counts = group_data["INT1_R"].value_counts().sort_index()
        results[group_name] = counts

    labels = {
        1: "Très intéressé",
        2: "Assez intéressé",
        3: "Peu intéressé",
        4: "Pas du tout intéressé"
    }
    results.index = [labels.get(i, i) for i in results.index]

    ax = results.plot(kind='bar', figsize=(10, 6), color=["green", "orange", "yellow", "red", "purple", "brown", "lightblue", "yellowgreen"])
    ax.set_title("Niveau d'intérêt pour l'information par groupe")
    ax.set_xlabel("Niveau d'intérêt")
    ax.set_ylabel("Nombre de réponses")
    ax.legend(title="Groupes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return ax.get_figure()

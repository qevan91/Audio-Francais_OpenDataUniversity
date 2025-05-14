import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_excel("data/les-francais-et-l-information-arcom-2024-base-anonymisee.xlsx", engine="openpyxl")

def plot_social_network_usage(data, selected_groups):
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
        counts = group_data["RSINFO_2_LR_R4"].value_counts().sort_index()
        results[group_name] = counts

    labels = {
        1: "Facebook", 2: "Instagram", 3: "X(Twitter)", 4: "Tiktok", 5: "Snapchat",
        6: "LinkdIn", 7: "WhatsApp", 8: "Telegram", 9: "Youtube", 10: "Reddit",
        11: "Discord", 12: "Twitch", 13: "Autre", 14: "Aucun"
    }
    results.index = [labels.get(i, i) for i in results.index]

    ax = results.plot(kind='bar', figsize=(10, 6),
                      color=["blue", "orange", "black", "red", "yellow", "blue", "green",
                             "blue", "red", "orange", "blue", "purple", "yellow", "gray"])
    ax.set_title("Plateformes utilisées pour s'informer selon le groupe social")
    ax.set_xlabel("Plateformes")
    ax.set_ylabel("Nombre de réponses")
    ax.legend(title="Groupes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return ax.get_figure()

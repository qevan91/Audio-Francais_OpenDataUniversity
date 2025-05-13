import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("data/les-francais-et-l-information-arcom-2024-base-anonymisee.xlsx", engine="openpyxl")

groups = {
    "Retraités": 6,
    "Employés": 1,
    "Étudiants": 4
}

results = pd.DataFrame()

for group_name, group_value in groups.items():
    group_data = data[data["RS3_R"] == group_value]
    counts = group_data["INT1_R"].value_counts().sort_index()
    results[group_name] = counts

labels = {1: "Très intéressé", 2: "Assez intéressé", 3: "Peu intéressé", 4: "Pas du tout intéressé"}
results.index = [labels[i] for i in results.index]

results.plot(kind='bar', figsize=(10, 6), color=["green", "orange", "yellow", "red"])
plt.title("Niveau d'intérêt pour l'information par groupe")
plt.xlabel("Niveau d'intérêt")
plt.ylabel("Nombre de réponses")
plt.xticks(rotation=45)
plt.legend(title="Groupes")
plt.tight_layout()
plt.savefig('graphe/interet_combined.png')
plt.show()
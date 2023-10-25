import tkinter as tk
from tkinter import scrolledtext


def create_ui(window):
    # Configuration de la fenêtre
    window.title("Mise à jour des fichiers XML")

    # Création des champs de texte pour chaque langue
    en_text = scrolledtext.ScrolledText(window, width=40, height=10)
    en_text.grid(column=0, row=0, padx=10, pady=10)
    en_label = tk.Label(window, text="Anglais")
    en_label.grid(column=0, row=1)

    de_text = scrolledtext.ScrolledText(window, width=40, height=10)
    de_text.grid(column=1, row=0, padx=10, pady=10)
    de_label = tk.Label(window, text="Allemand")
    de_label.grid(column=1, row=1)

    # ... Créez des champs et des étiquettes similaires pour chaque langue

    # Création du bouton de validation
    # Note: La commande sera définie dans main.py
    submit_button = tk.Button(window, text="Submit")
    submit_button.grid(column=0, row=2, columnspan=2, pady=20)

    return en_text, de_text, submit_button

# Vous pouvez également définir d'autres fonctions ou classes pour gérer
# des aspects plus avancés de l'interface utilisateur si nécessaire.

import tkinter as tk
from tkinter import scrolledtext


def create_ui(window):
    # Configuration de la fenêtre
    window.title("Mise à jour des fichiers XML")

    # Création du label et du champ d'entrée pour la clé de traduction
    translation_key_label = tk.Label(window, text="Clé de traduction")
    translation_key_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=10)

    translation_key_entry = tk.Entry(window, width=30)
    translation_key_entry.grid(column=1, row=0, padx=10, pady=10)

    # Création des champs de texte pour chaque langue
    en_text = scrolledtext.ScrolledText(window, width=40, height=10)
    en_text.grid(column=0, row=1, padx=10, pady=10)
    en_label = tk.Label(window, text="Anglais")
    en_label.grid(column=0, row=2)

    de_text = scrolledtext.ScrolledText(window, width=40, height=10)
    de_text.grid(column=1, row=1, padx=10, pady=10)
    de_label = tk.Label(window, text="Allemand")
    de_label.grid(column=1, row=2)

    fr_text = scrolledtext.ScrolledText(window, width=40, height=10)
    fr_text.grid(column=2, row=1, padx=10, pady=10)
    fr_label = tk.Label(window, text="Francais")
    fr_label.grid(column=2, row=2)

    pt_text = scrolledtext.ScrolledText(window, width=40, height=10)
    pt_text.grid(column=0, row=3, padx=10, pady=10)
    pt_label = tk.Label(window, text="Portugais")
    pt_label.grid(column=0, row=4)

    nl_text = scrolledtext.ScrolledText(window, width=40, height=10)
    nl_text.grid(column=1, row=3, padx=10, pady=10)
    nl_label = tk.Label(window, text="Neerlandais")
    nl_label.grid(column=1, row=4)

    ja_text = scrolledtext.ScrolledText(window, width=40, height=10)
    ja_text.grid(column=2, row=3, padx=10, pady=10)
    ja_label = tk.Label(window, text="Japonais")
    ja_label.grid(column=2, row=4)

    it_text = scrolledtext.ScrolledText(window, width=40, height=10)
    it_text.grid(column=0, row=5, padx=10, pady=10)
    it_label = tk.Label(window, text="Italien")
    it_label.grid(column=0, row=6)

    # ... Créez des champs et des étiquettes similaires pour chaque langue

    # Création du bouton de validation
    # Note: La commande sera définie dans main.py
    submit_button = tk.Button(window, text="Submit")
    submit_button.grid(column=0, row=7, columnspan=2, pady=20)

    return en_text, de_text, fr_text, pt_text, nl_text, ja_text, it_text, submit_button

# Vous pouvez également définir d'autres fonctions ou classes pour gérer
# des aspects plus avancés de l'interface utilisateur si nécessaire.

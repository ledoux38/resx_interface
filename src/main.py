import tkinter as tk
import xml.etree.ElementTree as ET

from config_handler import load_config
from ui import create_ui


def update_file(lang, data_block):
    file_path = f'{lang}.xml'
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        new_data = ET.fromstring(data_block)
        root.append(new_data)
        tree.write(file_path)
    except Exception as e:
        print(f'Erreur lors de la mise à jour du fichier {file_path}: {e}')


def on_submit():
    data_blocks = {
        'en': en_text.get("1.0", 'end-1c'),
        'de': de_text.get("1.0", 'end-1c'),
        'fr': fr_text.get("1.0", 'end-1c'),
        'it': it_text.get("1.0", 'end-1c'),
        'pt': pt_text.get("1.0", 'end-1c'),
        'ja': ja_text.get("1.0", 'end-1c'),
        'nl': nl_text.get("1.0", 'end-1c'),
        # ... autres langues
    }

    for lang, data_block in data_blocks.items():
        update_file(lang, data_block)


if __name__ == "__main__":
    # Charger la configuration au démarrage de l'application
    config = load_config()

    if config is None:
        print("Erreur de configuration. Arrêt du programme.")
        exit(1)  # Exit the program with an error code

    # Utiliser la configuration dans votre application
    translation_files = config['translation_files']

    window = tk.Tk()
    en_text, de_text, fr_text, it_text, pt_text, ja_text, nl_text, submit_button = create_ui(window)
    window.mainloop()

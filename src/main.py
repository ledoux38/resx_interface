import tkinter as tk
from tkinter import scrolledtext
import xml.etree.ElementTree as ET
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
        # ... autres langues
    }

    for lang, data_block in data_blocks.items():
        update_file(lang, data_block)


if __name__ == "__main__":
    window = tk.Tk()
    en_text, de_text, submit_button = create_ui(window)
    window.mainloop()

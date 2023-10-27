import json
import platform


def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier de configuration: {e}")
        return None


# Déterminer la plateforme
is_windows = platform.system() == 'Windows'

# Choisir le fichier de configuration en fonction de la plateforme
config_file = 'config_windows.json' if is_windows else 'config_linux.json'

# Charger la configuration
config = load_config(config_file)

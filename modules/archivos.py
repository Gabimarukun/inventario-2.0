import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FILE_PATH = os.path.join(DATA_DIR, 'datos.txt')

def check_files():
    """Asegura que la carpeta data y el archivo datos.txt existan"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            # Guarda un array vacío por defecto usando json
            json.dump([], file)

def load_data():
    """Carga los datos desde el archivo de texto en formato JSON"""
    check_files()
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            # Si el archivo está vacío o dañado
            return []

def save_data(data):
    """Guarda los datos listados en el archivo de texto"""
    check_files()
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

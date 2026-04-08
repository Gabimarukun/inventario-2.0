import os

def limpiar_pantalla():
    """Limpia la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

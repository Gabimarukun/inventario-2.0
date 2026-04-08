from .operaciones import crear_registro, consultar_registros, editar_registro, eliminar_registro
from .reportes import reporte_inventario
from utils.helpers import limpiar_pantalla
from utils.config import config

def mostrar_menu():
    """Bucle principal que muestra el menú y permite navegar entre opciones"""
    while True:
        limpiar_pantalla()
        print(f"\n=== {config['app_name']} (v{config['version']}) ===")
        print("1. Crear nuevo registro")
        print("2. Consultar registros")
        print("3. Editar registro")
        print("4. Eliminar registro")
        print("5. Ver reporte de sistema")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")
        
        limpiar_pantalla()
        
        if opcion == '1':
            crear_registro()
        elif opcion == '2':
            consultar_registros()
        elif opcion == '3':
            editar_registro()
        elif opcion == '4':
            eliminar_registro()
        elif opcion == '5':
            reporte_inventario()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            
        if opcion != '6':
            input("\nPresione Enter para continuar...")

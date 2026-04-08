from .archivos import load_data, save_data
from .validaciones import validate_empty, validate_integer, validate_float
from utils.config import config

def generate_id(data):
    """Genera un nuevo ID autoincremental basado en los existentes"""
    if not data:
        return 1
    return max(item['id'] for item in data) + 1

def crear_registro():
    """CREAR: Solicita los datos y crea un nuevo registro (producto)"""
    print("--- Nuevo Registro ---")
    
    nombre = input("Ingrese el nombre del artículo: ")
    while not validate_empty(nombre):
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del artículo: ")

    precio_str = input("Ingrese el precio: ")
    while not validate_float(precio_str):
        print("Precio inválido. Debe ser un número.")
        precio_str = input("Ingrese el precio: ")
    precio = float(precio_str)

    cantidad_str = input("Ingrese la cantidad: ")
    while not validate_integer(cantidad_str):
        print("Cantidad inválida. Debe ser un entero.")
        cantidad_str = input("Ingrese la cantidad: ")
    cantidad = int(cantidad_str)

    data = load_data()
    nuevo_id = generate_id(data)
    
    # Lista
    nuevo_registro = {
        'id': nuevo_id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    
    data.append(nuevo_registro)
    save_data(data)
    print("¡Registro creado exitosamente!")

def consultar_registros():
    """LEER: Muestra en pantalla todos los registros guardados"""
    print("--- Lista de Registros ---")
    data = load_data()
    
    if not data:
        print("No hay registros en el sistema.")
        return False
        
    for item in data:
        print(f"ID: {item['id']} | Nombre: {item['nombre']} | Precio: {config['currency']}{item['precio']} | Cantidad: {item['cantidad']}")
    return True

def editar_registro():
    """ACTUALIZAR: Permite buscar por ID y modificar los campos"""
    print("--- Editar Registro ---")
    
    if not consultar_registros():
        return
        
    id_str = input("\nIngrese el ID del registro a editar: ")
    if not validate_integer(id_str):
        print("El ID ingresado es inválido.")
        return
    
    registro_id = int(id_str)
    data = load_data()
    
    for item in data:
        if item['id'] == registro_id:
            print(f"\nEditando registro: {item['nombre']}")
            
            nuevo_nombre = input(f"Nuevo nombre (actual: {item['nombre']}, Enter para saltar): ")
            if validate_empty(nuevo_nombre):
                item['nombre'] = nuevo_nombre
                
            nuevo_precio = input(f"Nuevo precio (actual: {item['precio']}, Enter para saltar): ")
            if validate_empty(nuevo_precio) and validate_float(nuevo_precio):
                item['precio'] = float(nuevo_precio)
                
            nueva_cantidad = input(f"Nueva cantidad (actual: {item['cantidad']}, Enter para saltar): ")
            if validate_empty(nueva_cantidad) and validate_integer(nueva_cantidad):
                item['cantidad'] = int(nueva_cantidad)
                
            save_data(data)
            print("¡Registro actualizado exitosamente!")
            return
            
    print("No se encontró ningún registro con ese ID.")

def eliminar_registro():
    """ELIMINAR: Permite buscar por ID y borrar el elemento de la lista"""
    print("--- Eliminar Registro ---")
    
    if not consultar_registros():
        return
        
    id_str = input("\nIngrese el ID del registro a eliminar: ")
    if not validate_integer(id_str):
        print("El ID ingresado es inválido.")
        return
    
    registro_id = int(id_str)
    data = load_data()
    
    for i, item in enumerate(data):
        if item['id'] == registro_id:
            confirmacion = input(f"¿Seguro que desea eliminar el registro '{item['nombre']}'? (s/n): ")
            if confirmacion.lower() == 's':
                data.pop(i)
                save_data(data)
                print("¡Registro eliminado exitosamente!")
            else:
                print("Operación cancelada.")
            return
            
    print("No se encontró ningún registro con ese ID.")

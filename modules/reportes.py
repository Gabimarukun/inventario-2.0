from .archivos import load_data
from utils.config import config

def reporte_inventario():
    """Genera un reporte resumido leyendo los datos de los registros"""
    data = load_data()
    
    if not data:
        print("\nNo hay datos para generar el reporte.")
        return
        
    total_registros = len(data)
    total_piezas = sum(item['cantidad'] for item in data)
    valor_total_inventario = sum(item['precio'] * item['cantidad'] for item in data)
    
    print("\n========= REPORTE GENERAL =========")
    print(f"Total de productos diferentes:  {total_registros}")
    print(f"Total de artículos físicos:     {total_piezas}")
    print(f"Valor monetario total:         {config['currency']}{valor_total_inventario:,.2f}")
    print("===================================")

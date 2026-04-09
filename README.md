# Sistema de Gestión de Inventario (CRUD)

Este es un sistema de gestión de inventario básico desarrollado en **Python** que funciona a través de la terminal (consola). El proyecto sigue una estructura modular y permite realizar las operaciones fundamentales de un CRUD (Crear, Leer, Actualizar y Eliminar).

## Características

- **Modular:** Código organizado en diferentes archivos para facilitar mantenimiento.
- **Persistencia de Datos:** Los registros se guardan en un archivo de texto (`data/datos.txt`) en formato JSON.
- **Validación:** Asegura que los datos ingresados (precios, cantidades, nombres) sean correctos.
- **Reporte:** Cálculo automático del valor total del inventario.
- **Configuración:** Fácil personalización del nombre de la app, moneda y versión.

##  Estructura del Proyecto

```text
├── main.py                 # Punto de entrada de la aplicación
├── data/
│   └── datos.txt           # Archivo donde se guardan los datos
├── modules/
│   ├── archivos.py         # Carga y guardado en disco
│   ├── menu.py             # Lógica del menú principal
│   ├── operaciones.py      # Lógica de CRUD (crear, editar, etc.)
│   ├── reportes.py         # Generación de estadísticas
│   └── validaciones.py     # Comprobación de tipos de datos
└── utils/
    ├── config.py           # Diccionario con configuración global
    └── helpers.py          # Funciones de utilidad (limpiar pantalla)
```

## Conceptos Programación Utilizados

Este proyecto sirve como práctica de conceptos fundamentales en Python:
- **Programación Modular:** Dividir el código en funciones y archivos.
- **Estructuras de Datos:** Uso de listas y diccionarios.
- **Operadores:** Uso de operadores aritméticos, de comparación y lógicos.
- **Manejo de Archivos:** Lectura y escritura de archivos.

## Cómo Ejecutarlo

1. Asegúrate de tener Python instalado en tu PC.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Ejecuta el comando:
   ```
   python main.py o python3 main.py en linux
   ```

---
*Desarrollado por Luis Colina 30400695, Rafael Velasco 31577792  y Carlos Molina 28774022*

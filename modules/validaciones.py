def validate_empty(text):
    """Valida que un texto no sea vacío"""
    return len(text.strip()) > 0

def validate_integer(value):
    """Valida que el valor pueda convertirse a un entero"""
    try:
        int(value)
        return True
    except ValueError:
        return False

def validate_float(value):
    """Valida que el valor pueda convertirse a decimal (float)"""
    try:
        float(value)
        return True
    except ValueError:
        return False

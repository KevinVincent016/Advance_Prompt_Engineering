def validar_contrasena(contrasena):
    """
    Valida una contraseña según criterios de seguridad definidos.

    Reglas de validación:
    1. Debe tener al menos 12 caracteres de longitud.
    2. Debe contener al menos una letra mayúscula (A-Z).
    3. Debe contener al menos una letra minúscula (a-z).
    4. Debe contener al menos un número (0-9).
    5. Debe contener al menos un carácter especial (por ejemplo: @, #, $, %, &, !).

    Parámetros:
        contrasena (str): La contraseña a validar.

    Retorna:
        bool: True si la contraseña cumple con todos los criterios, False en caso contrario.
    """
    if len(contrasena) < 12:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    caracteres_especiales = "@#$%&!"

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True

    return all([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial])


# Ejemplos de uso:

# Ejemplo 1: Contraseña válida
print(validar_contrasena("ClaveSegura2023!"))  # True

# Ejemplo 2: Contraseña demasiado corta
print(validar_contrasena("Clav3!"))  # False

# Ejemplo 3: Falta de carácter especial
print(validar_contrasena("PasswordSegura2023"))  # False

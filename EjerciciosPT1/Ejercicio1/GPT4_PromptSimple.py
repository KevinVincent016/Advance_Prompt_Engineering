import re

def validar_contraseña(contraseña):
    """
    Valida una contraseña según los siguientes criterios:
    - Mínimo 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    """

    if len(contraseña) < 8:
        return "❌ La contraseña debe tener al menos 8 caracteres."

    if not re.search(r"[A-Z]", contraseña):
        return "❌ La contraseña debe contener al menos una letra mayúscula."

    if not re.search(r"[a-z]", contraseña):
        return "❌ La contraseña debe contener al menos una letra minúscula."

    if not re.search(r"\d", contraseña):
        return "❌ La contraseña debe contener al menos un número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        return "❌ La contraseña debe contener al menos un carácter especial."

    return "✅ Contraseña válida."

# Ejemplo de uso
print(validar_contraseña("Abc123!@#"))  # Debería devolver "✅ Contraseña válida."

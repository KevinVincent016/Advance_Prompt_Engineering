# Ejercicio 1: Generación de una Función de Código

**Objetivo:** Crear una función en Python que valide si una contraseña cumple con ciertos criterios de seguridad.

## Prompts para el modelo

**Modelo:** GPT-4

### Prompt Simple

```
Haz una función en Python para validar una contraseña.
```

### Prompt Avanzado

```
**Rol:** Eres un desarrollador de software senior especializado en ciberseguridad.

**Tarea:** Genera una función en Python llamada `validar_contrasena`.

**Contexto:** La función recibirá una cadena de texto (la contraseña) y debe retornar `True` si cumple con TODAS las siguientes reglas, o `False` si falla al menos una.

**Reglas de Validación (Criterios):**
1.  Debe tener una longitud mínima de 12 caracteres.
2.  Debe contener al menos una letra mayúscula (A-Z).
3.  Debe contener al menos una letra minúscula (a-z).
4.  Debe contener al menos un número (0-9).
5.  Debe contener al menos un carácter especial (ej: @, #, $, %, &, !).

**Formato de Salida:**
-   El bloque de código de la función en Python.
-   Debe incluir docstrings que expliquen qué hace la función, sus parámetros y qué retorna.
-   Añade 3 ejemplos de uso: uno con una contraseña válida y dos con contraseñas inválidas que demuestren diferentes fallos.

**Restricciones:**
-   No uses librerías externas, solo el core de Python.
-   El código debe ser legible y seguir las convenciones de estilo de PEP 8.
```

## Respuestas del modelo

### Prompt Simple

```
Claro, aquí tienes una función en Python para validar una contraseña según criterios comunes de seguridad. Puedes modificar las reglas según tus necesidades.

🎯 Requisitos de la contraseña:

Al menos 8 caracteres

Al menos una letra mayúscula

Al menos una letra minúscula

Al menos un número

Al menos un carácter especial (como @, #, $, etc.)

✅ Función en Python:

[[Revisar y probar codigo en el archivo GPT4_PromptSimple.py]]

¿Quieres que adapte la función a otros criterios? Por ejemplo, longitud mínima diferente, prohibir espacios, etc.

```

### Prompt Avanzado

```
Aquí tienes la función validar_contrasena en Python, implementada según tus requisitos y siguiendo buenas prácticas de ciberseguridad y estilo:

[[Revisar y probar codigo en el archivo GPT4_PromptAvanzado.py]]

Explicación rápida de los ejemplos:

Ejemplo 1: Cumple todos los requisitos (mayúsculas, minúsculas, números, carácter especial, longitud ≥ 12).

Ejemplo 2: Tiene todos los tipos de caracteres pero solo 6 caracteres → inválida.

Ejemplo 3: No contiene ningún carácter especial → inválida.

¿Deseas que el sistema indique cuál regla falló en lugar de solo retornar False? También puedo hacer eso.

```


## Evaluación Comparativa

-   **Completitud:** ¿La función del prompt simple incluyó todas las reglas?
-   **Claridad:** ¿El código está bien documentado? ¿Es fácil de entender?
-   **Utilidad:** ¿El prompt avanzado proporcionó ejemplos de uso que facilitan la prueba y la integración?
-   **Robustez:** ¿La función maneja casos borde que el prompt simple podría haber ignorado?


### Completitud

La funcion con el prompt simple intuyo las mismas reglas que se definen en el prompt avanzado pero no fue muy detallado en la regla de los caracteres especiales ya que tomo una lista mayor de caracteres, en cuanto al codigo, genero un codigo sencillo, con una documentacion corta y solo un ejemplo practico, la salida es corresta y el metodo retorna True o False

Por otro lado la respuesta dada con el prompt avanzado cumple rigurosamente con las especificaciones otorgadas, tambien incluye una documentacion un poco mas detallada y incluye los 3 casos de prueba del metodo

En ambos casos la funcion de python funciona.

### Claridad

En ambos casos el codigo es legible y facil de entender, tanto con el prompt simple como el avanzado añadieron documentacion al inicio de la función, la diferencia radica en que tan especificos son, donde el prompt simple solamente se limito a redactar las reglas sencillas que siguio y el prompt avanzado detallo mas las reglas, parametros y el retorno de la funcion

### Utilidad

En ambos casos se planteo ejemplos para validar la utilidad de la funcion, el prompt simple otrogo un solo ejemplo de uso donde se cumplian todas las reglas y la funcion retornaba True, por otro lado el prompt complejo siguio las indicaciones y añadio 3 ejemplos de uso donde uno funcionaba y retornaba true y los otros 2 fallaban, mostrando asi el funcionamiento de la funcion

### Robustez

En el caso del prompt simple, el caos de ejemplo no aborda situaciones diferentes que puedan causar problemas con la contraseña, solamente sigue las instrucciones para generar una contraseña que cumpla con todas las validaciones y retorne True (Happy Path). Por otro lado, el prompt avanzado cubre algunos casos en los ejemplos que plantea, aborda una contraseña correcta, tambien una contraseña corta y una contraseña que no incluye caracteres especiales, asi abordando algunos casos a los que se puede enfrentar la función
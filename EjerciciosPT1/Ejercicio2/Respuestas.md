# Ejercicio 1: Generación de una Función de Código

**Objetivo:** Extraer datos específicos de un texto no estructurado y presentarlos en formato JSON.

## Prompts para el modelo

**Modelo:** GPT-4

### Prompt Simple

```
Saca los datos importantes de este texto en JSON:

"La reunión de lanzamiento del Proyecto Fénix será el 15 de octubre de 2024 a las 10:30 AM en la Sala Júpiter. Los asistentes confirmados son Ana García (Líder de Proyecto), Carlos Rodríguez (Desarrollador Principal) y Elena Fernández (Diseñadora UX). El presupuesto asignado es de $25,000 USD."
```

### Prompt Avanzado

```
**Rol:** Eres un asistente de procesamiento de datos altamente preciso.

**Tarea:** Extrae la información clave del siguiente texto y formatéala estrictamente como un objeto JSON.

**Texto de Entrada:**
```
La reunión de lanzamiento del Proyecto Fénix será el 15 de octubre de 2024 a las 10:30 AM en la Sala Júpiter. Los asistentes confirmados son Ana García (Líder de Proyecto), Carlos Rodríguez (Desarrollador Principal) y Elena Fernández (Diseñadora UX). El presupuesto asignado es de $25,000 USD.
```

**Esquema JSON de Salida (Schema):**
Debes seguir esta estructura exacta. Si un campo no se encuentra en el texto, déjalo como `null`.

```json
{
  "proyecto": {
    "nombre": "string",
    "presupuesto": {
      "monto": "number",
      "moneda": "string"
    }
  },
  "reunion": {
    "fecha": "string (formato YYYY-MM-DD)",
    "hora": "string (formato HH:MM)",
    "ubicacion": "string"
  },
  "asistentes": [
    {
      "nombre": "string",
      "rol": "string"
    }
  ]
}
```

## Respuestas del modelo

### Prompt Simple

```
Aquí tienes los datos importantes del texto en formato JSON:

{
  "proyecto": "Fénix",
  "evento": "Reunión de lanzamiento",
  "fecha": "2024-10-15",
  "hora": "10:30 AM",
  "lugar": "Sala Júpiter",
  "asistentes": [
    {
      "nombre": "Ana García",
      "rol": "Líder de Proyecto"
    },
    {
      "nombre": "Carlos Rodríguez",
      "rol": "Desarrollador Principal"
    },
    {
      "nombre": "Elena Fernández",
      "rol": "Diseñadora UX"
    }
  ],
  "presupuesto": {
    "monto": 25000,
    "moneda": "USD"
  }
}

¿Quieres que lo guarde en un archivo o lo convierta a otro formato?
```

### Prompt Avanzado

```
{
  "proyecto": {
    "nombre": "Proyecto Fénix",
    "presupuesto": {
      "monto": 25000,
      "moneda": "USD"
    }
  },
  "reunion": {
    "fecha": "2024-10-15",
    "hora": "10:30",
    "ubicacion": "Sala Júpiter"
  },
  "asistentes": [
    { 
      "nombre": "Ana García",
      "rol": "Líder de Proyecto"
    },
    {
      "nombre": "Carlos Rodríguez",
      "rol": "Desarrollador Principal"
    },
    {
      "nombre": "Elena Fernández",
      "rol": "Diseñadora UX"
    }
  ]
}

```


## Evaluación Comparativa

-   **Estructura:** ¿El JSON del prompt simple tiene una estructura lógica y predecible?
-   **Precisión:** ¿Los tipos de datos son correctos (números vs. strings)?
-   **Parseabilidad:** ¿El JSON generado por el prompt avanzado es directamente utilizable por una aplicación sin necesidad de limpieza o conversión?
-   **Manejo de Nulos:** ¿Cómo manejaría cada uno un texto donde, por ejemplo, el presupuesto no se menciona?


### Estructura

El prompt simple cuenta con una estructura predecible, es sencilla y directa con la información. Logro identificar la información clave y agruparla en el JSON de forma correcta.

### Precisión

En ambas respuestas los datos son correctos con una pequeña diferencia, en el prompt simple la hora se especifica en formato 24hrs debido a que indica el "AM" luego del valor, mientras que en el prompt avanzado solamente indica la hora "10:30"

### Parseabilidad

Si, el prompt avanzado es directamente utilizable en una aplicacion ya que este esta bien estructurado y es posible acceder a los datos con consultas sencillas al igual que es posible añadir mas información sin comprometer la estructura del JSON.

### Manejo de Nulos

Dentro de los prompt especificados no se da un caso donde se deba registrar un valor nulo, pero siguiendo las instrucciones indicadas, el prompt avanzado podria manejar los nulos simplemente escribiendo "null" en el espacio, por otro lado se espera que el prompt simple haga lo mismo pero debido a que no se indico dicha regla es posible que omita la información y no la escriba
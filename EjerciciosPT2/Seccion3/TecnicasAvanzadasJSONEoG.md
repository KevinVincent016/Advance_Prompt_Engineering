### 3.5 JSON Enforced Output & Guardrails

#### Ejercicio 7B: Extracción de Contactos

Texto de entrada:
“Juan Pérez vive en Bogotá, Colombia. Su correo es [juanperez@mail.com](mailto:juanperez@mail.com) y su teléfono es +57 300 123 4567.”

Prompt:

```
Extrae la información y responde solo con un JSON válido en esta estructura:  

{
  "nombre": "string",
  "ciudad": "string",
  "pais": "string",
  "email": "string",
  "telefono": "string"
}
```

Esto asegura que la salida sea **estructurada y usable por un sistema**.

---

#### Puesta en practica

##### GPT-4

```text
{
  "nombre": "Juan Pérez",
  "ciudad": "Bogotá",
  "pais": "Colombia",
  "email": "juanperez@mail.com",
  "telefono": "+57 300 123 4567"
}
```
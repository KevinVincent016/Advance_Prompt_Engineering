## Sección 2: Diseño de Prompts Estructurados y Reutilizables (Plantillas)

### Ejercicio 2B: Plantilla para Resumir Artículos Científicos

```text
# Identidad
Eres un investigador que resume artículos científicos para estudiantes universitarios.

# Instrucciones
- Haz un resumen de máximo 150 palabras.
- Usa un lenguaje accesible pero formal.
- Incluye: objetivo, método y conclusión principal.

# Contexto del Artículo
<articulo>
    <titulo>{{titulo}}</titulo>
    <autor>{{autor}}</autor>
    <tema>{{tema}}</tema>
</articulo>

Genera el resumen basado en el contexto.
```

**Ejemplo de uso:**

* Título: “Aplicaciones de la IA en medicina”
* Autor: “Dra. López”
* Tema: “Diagnóstico asistido por IA”

---

### Ejercicio 2C: Plantilla para Emails Profesionales

```text
# Identidad
Eres un asistente ejecutivo especializado en comunicación corporativa.

# Instrucciones
- Redacta un email breve, claro y profesional.
- Usa tono cordial pero directo.
- Incluye saludo, cuerpo y cierre con firma.

# Contexto
<email>
    <destinatario>{{nombre}}</destinatario>
    <asunto>{{asunto}}</asunto>
    <puntos_clave>{{puntos}}</puntos_clave>
</email>
```

Esto permite automatizar **múltiples correos** con la misma calidad estructural.

---


## Puesta en practica

### Modelo utilizado

**Modelo:** GPT-4

### Respuestas

#### Plantilla para Resumir Artículos Científicos

```text
# Identidad
Eres un investigador que resume artículos científicos para estudiantes universitarios.

# Instrucciones
- Haz un resumen de máximo 150 palabras.
- Usa un lenguaje accesible pero formal.
- Incluye: objetivo, método y conclusión principal.

# Contexto del Artículo
<articulo>
    <titulo>{{titulo}}</titulo>
    <autor>{{autor}}</autor>
    <tema>{{tema}}</tema>
</articulo>

Genera el resumen basado en el contexto.
```

**Ejemplo de uso:**

* Título: “Aplicaciones de la IA en medicina”
* Autor: “Dra. López”
* Tema: “Diagnóstico asistido por IA”

```text
Resumen del artículo “Aplicaciones de la IA en medicina” – Dra. López

El artículo explora cómo la inteligencia artificial (IA) está transformando el diagnóstico médico. El objetivo principal es analizar el uso de sistemas de IA para mejorar la precisión y rapidez en la identificación de enfermedades. La Dra. López describe diversos métodos, como el aprendizaje automático y las redes neuronales, aplicados al análisis de imágenes médicas, historiales clínicos y patrones de síntomas. Estos sistemas permiten a los profesionales detectar afecciones como cáncer, enfermedades cardiovasculares y trastornos neurológicos con mayor eficacia. La conclusión principal es que, aunque la IA no reemplaza al personal médico, sí representa una herramienta valiosa para apoyar el diagnóstico clínico, reducir errores y optimizar la toma de decisiones. El artículo también destaca la necesidad de regulaciones éticas y formación especializada para una implementación segura y efectiva.
```

#### Plantilla para Emails Profesionales

```text
# Identidad
Eres un asistente ejecutivo especializado en comunicación corporativa.

# Instrucciones
- Redacta un email breve, claro y profesional.
- Usa tono cordial pero directo.
- Incluye saludo, cuerpo y cierre con firma.

# Contexto
<email>
    <destinatario>{{nombre}}</destinatario>
    <asunto>{{asunto}}</asunto>
    <puntos_clave>{{puntos}}</puntos_clave>
</email>
```

**Ejemplo de uso:**

* Destinatario: “Dra. López”
* Asunto: “La implicación de las IAs en un diagnostico rápido”
* Puntos Clave: “Diagnóstico asistido por IA, Riesgos de un diagnostico rápido, capacidad de analisis de la IA”

```text
Asunto: La implicación de las IAs en un diagnóstico rápido
Para: Dra. López

Estimada Dra. López,

Espero que se encuentre muy bien. Me permito escribirle para compartir algunos puntos clave sobre el uso de inteligencia artificial en diagnósticos médicos, con énfasis en su rapidez y precisión.

La incorporación de sistemas de IA en procesos diagnósticos ha demostrado mejorar significativamente la capacidad de análisis, permitiendo identificar patrones complejos en menos tiempo. No obstante, también es importante considerar los riesgos asociados a un diagnóstico acelerado, como posibles omisiones o sobredependencia de la tecnología.

Quedo a su disposición para profundizar en estos aspectos o coordinar una reunión si lo considera oportuno.

Saludos cordiales,
[Tu Nombre]
Asistente Ejecutivo – Comunicación Corporativa
```
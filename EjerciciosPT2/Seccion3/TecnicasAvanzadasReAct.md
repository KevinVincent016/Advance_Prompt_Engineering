### 3.2 ReAct

#### Ejercicio 4B: Simulación de búsqueda encadenada

**Pregunta:** “¿Cuál es la capital de Australia y en qué continente está?”

Prompt con ReAct:

```text
Thought: Necesito identificar la capital de Australia.  
Action: Search("capital de Australia")  
Observation: Canberra es la capital.  

Thought: Ahora debo identificar en qué continente está.  
Action: Search("Australia continente")  
Observation: Australia está en Oceanía.  

Final Answer: La capital de Australia es Canberra y el país se encuentra en Oceanía.
```

#### Puesta en practica

##### GPT-4 pregunta directa

```text
La capital de Australia es Canberra, aunque muchas personas tienden a pensar que la capital es Sídney o Melbourne, ya que son las ciudades más grandes y conocidas del país.

Australia está en el continente Oceanía. Es el país más grande del continente y también se le puede considerar un continente en sí mismo, ya que ocupa toda la tierra principal del continente australiano.
```

##### GPT-4 prompt ReAct

```text
¡Buen trabajo! La capital de Australia es efectivamente Canberra, y el país está ubicado en Oceanía. Si necesitas más detalles o tienes otra pregunta, ¡avísame!
```
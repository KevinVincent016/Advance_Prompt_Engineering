### 3.3 Self-Consistency

#### Ejercicio 5B: Pregunta Trampa de Probabilidad

“Si lanzas una moneda dos veces, ¿cuál es la probabilidad de obtener dos caras seguidas?”

* **Prompt:**

  ```
  Resuelve este problema paso a paso: Si lanzas una moneda dos veces, ¿cuál es la probabilidad de obtener dos caras seguidas?
  ```
    
Pide 3 cadenas de razonamiento independientes y compara:

* Algunos modelos dirán 1/2, otros 1/4.
* Con autoconsistencia, la mayoría coincidirá en 1/4 (correcto).

#### Puesta en practica

##### GPT-4

```
  Para resolver este problema, vamos a desglosarlo paso a paso.

Paso 1: Identificar todos los posibles resultados al lanzar una moneda dos veces

Cuando lanzamos una moneda dos veces, cada lanzamiento tiene dos resultados posibles: cara (C) o cruz (X).

Por lo tanto, los resultados posibles al lanzar la moneda dos veces son:

Cara, Cara (CC)

Cara, Cruz (CX)

Cruz, Cara (XC)

Cruz, Cruz (XX)

Así que los resultados posibles son 4 en total.

Paso 2: Identificar el evento que estamos buscando

Queremos encontrar la probabilidad de obtener dos caras seguidas. Esto significa que el resultado que estamos buscando es "CC" (Cara en el primer lanzamiento y Cara en el segundo).

Paso 3: Calcular la probabilidad

De los 4 resultados posibles (CC, CX, XC, XX), solo uno es el que cumple con la condición de obtener dos caras seguidas (CC). Entonces, la probabilidad de obtener dos caras seguidas es:

𝑃(Dos caras seguidas)= numero de resultados favorables / Numero total de resultados posibles = 1/4

Respuesta

La probabilidad de obtener dos caras seguidas al lanzar una moneda dos veces es 
1/4 o 0.25, lo que equivale al 25%.
```

##### Gemini IA

```
  Aquí está la resolución paso a paso:

1. Determinar el Espacio Muestral
El espacio muestral (Ω) es el conjunto de todos los resultados posibles al realizar un experimento. Al lanzar una moneda dos veces, los posibles resultados son:

Cara en el primer lanzamiento (C) y Cara en el segundo (C) → CC

Cara en el primer lanzamiento (C) y Cruz en el segundo (X) → CX

Cruz en el primer lanzamiento (X) y Cara en el segundo (C) → XC

Cruz en el primer lanzamiento (X) y Cruz en el segundo (X) → XX

El número total de resultados posibles es N(Ω)=4.

2. Identificar el Evento Favorable
El evento favorable (A) es el resultado específico que queremos obtener, que en este caso es obtener dos caras seguidas.

Evento favorable (A) → CC

El número de resultados favorables es N(A)=1.

3. Calcular la Probabilidad
La probabilidad (P) de que ocurra un evento se calcula con la fórmula:

P(A)= Numero de resultados favorables / Numero total de resultados posibles = N(A) / N(Ω)
​
 
Sustituyendo los valores:

P(CC)= 1/4
​
 
4. (Método Alternativo) Probabilidad de Eventos Independientes
Como alternativa, se puede usar la regla de la multiplicación para eventos independientes.

La probabilidad de obtener Cara en un solo lanzamiento es P(C)=1/2.

El primer lanzamiento y el segundo lanzamiento son eventos independientes (el resultado de uno no afecta al otro).

La probabilidad de que ambos eventos independientes ocurran (obtener CC) es el producto de sus probabilidades individuales:

P(CC)=P(C en 1er lanzamiento)×P(C en 2do lanzamiento)
P(CC)= 1/2 × 1/2 = 1/4
​
 
Conversión a Porcentaje
Para expresar la probabilidad en porcentaje:

1/4 = 0.25

0.25 × 100% = 25%
```

##### Claude IA

```
  Voy a resolver este problema de probabilidad paso a paso.
Paso 1: Identificar el experimento

Lanzamos una moneda dos veces
Queremos encontrar la probabilidad de obtener dos caras seguidas (CC)

Paso 2: Determinar todos los resultados posibles
Al lanzar una moneda dos veces, los resultados posibles son:

CC (cara, cara)
CS (cara, sello)
SC (sello, cara)
SS (sello, sello)

Total de resultados posibles: 4
Paso 3: Identificar los resultados favorables
Los resultados que nos interesan (dos caras seguidas):

CC

Total de resultados favorables: 1
Paso 4: Calcular la probabilidad
La probabilidad se calcula como:
P(dos caras) = Resultados favorables / Resultados posibles totales
P(dos caras) = 1/4 = 0.25 = 25%
Verificación alternativa:
También podemos calcularlo usando la regla de multiplicación:

P(cara en primer lanzamiento) = 1/2
P(cara en segundo lanzamiento) = 1/2
P(cara Y cara) = 1/2 × 1/2 = 1/4

Respuesta: La probabilidad de obtener dos caras seguidas al lanzar una moneda dos veces es 1/4 o 25%.
```
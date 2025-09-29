## 3.1 Chain-of-Thought (CoT)

#### Ejercicio 3B: Problema Matemático

* **Prompt Directo:**

  ```
  ¿Cuál es la raíz cuadrada de 1764?
  ```
* **Prompt con CoT:**

  ```
  Calcula la raíz cuadrada de 1764. Piensa paso a paso, muestra tu razonamiento y luego la respuesta final.
  ```

Esto obliga al modelo a hacer la división en pasos (1764 ÷ 42 = 42), reduciendo errores.

---

#### Puesta en practica

##### Prompt Directo

```
  ¿Cuál es la raíz cuadrada de 1764?
```

```
  La raíz cuadrada de 1764 es 42.

📌 Porque:

42 × 42 = 1764

¿Quieres que te muestre cómo calcularla paso a paso?
```

##### Prompt con CoT

```
  Calcula la raíz cuadrada de 1764. Piensa paso a paso, muestra tu razonamiento y luego la respuesta final.
```

```
  Vamos a calcular la raíz cuadrada de 1764 paso a paso.

Paso 1: Estimar la raíz cuadrada

Buscamos un número cuyo cuadrado se acerque a 1764.
Sabemos que:

40^2 = 1600

50^2 = 2500

Entonces, la raíz cuadrada de 1764 está entre 40 y 50.

Probamos con algunos valores entre 40 y 50.

Paso 2: Probar con valores cercanos

42^2 = 42 × 42 = 1764

¡Perfecto! Lo hemos encontrado.

✅ Resultado final:
sqrt(1764) = 42​

```


#### Ejercicio 3C: Pregunta de Razonamiento

* **Directo:**

  ```
  María tiene el doble de edad que Juan. Juan tiene 12 años. ¿Qué edad tiene María?
  ```
* **Con CoT:**

  ```
  María tiene el doble de edad que Juan. Juan tiene 12 años. Razona paso a paso para calcular la edad de María y luego da la respuesta final.
  ```

---

#### Puesta en practica

##### Prompt Directo

```text
  María tiene el doble de edad que Juan. Juan tiene 12 años. ¿Qué edad tiene María?
```

```
Si Juan tiene 12 años y María tiene el doble de su edad, entonces:

Edad de María = 2 × 12 = 24

María tiene 24 años. ✅

```

##### Prompt con CoT

```
María tiene el doble de edad que Juan. Juan tiene 12 años. Razona paso a paso para calcular la edad de María y luego da la respuesta final.
```

```
Vamos a resolver el problema paso a paso:

🔢 Paso 1: Identificar la edad de Juan

Nos dicen que Juan tiene 12 años.

🧠 Paso 2: Entender la relación entre María y Juan

También nos dicen que María tiene el doble de edad que Juan.

Eso significa que debemos multiplicar la edad de Juan por 2 para encontrar la edad de María.

✖️ Paso 3: Calcular la edad de María
Edad de María = 2 × Edad de Juan = 2 × 12 = 24

✅ Respuesta final:

María tiene 24 años.
```
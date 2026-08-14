# Enteros grandes en Python

En esta parte practico una diferencia importante entre Python y lenguajes que
usan enteros de 32 o 64 bits. El tipo `int` de Python no tiene un máximo fijo:
puede crecer mientras la computadora tenga memoria disponible.

## Práctica 1: precisión arbitraria

El archivo `01_precision_arbitraria.py` compara números de distintos tamaños.
Uso `bit_length()` para ver cuántos bits necesita el valor y `sys.getsizeof()`
para observar que un entero más grande también ocupa más memoria.

```powershell
python 02_enteros_grandes/01_precision_arbitraria.py
```

Lo que entendí es que Python evita el desbordamiento de sus enteros aumentando
el espacio reservado. Esto es cómodo, aunque los cálculos enormes consumen más
memoria y tiempo.

## Práctica 2: qué significa `sys.maxsize`

`02_sys_maxsize.py` calcula valores mayores que `sys.maxsize`. Así comprobé que
ese dato no es el entero máximo de Python: está relacionado con el mayor índice
o tamaño que maneja la implementación en esta computadora.

```powershell
python 02_enteros_grandes/02_sys_maxsize.py
```

## Práctica 3: potencia modular

`03_potencia_modular.py` usa `pow(base, exponente, modulo)` para obtener un
código corto de equipo. Esta forma es más eficiente que construir primero una
potencia de millones de cifras y aplicar `%` después.

```powershell
python 02_enteros_grandes/03_potencia_modular.py
```

## Práctica 4: raíces enteras y factoriales

En `04_raices_y_factoriales.py` uso `math.isqrt()` para comprobar cuadrados
perfectos sin pasar por un `float`. También calculo `1000!` y cuento sus dígitos
para ver un entero enorme sin llenar la terminal con todo su contenido.

```powershell
python 02_enteros_grandes/04_raices_y_factoriales.py
```

## Práctica 5: desbordamiento e infinito

`05_desbordamiento_y_infinito.py` compara el resultado de `127 + 1` usando un
`int` normal y un entero de 8 bits. Uso `ctypes` para reproducir, sin instalar
NumPy, el comportamiento de ancho fijo que también hay que vigilar en NumPy y
pandas. Además compruebo que `float("inf")` es un `float`, no el máximo `int`.

```powershell
python 02_enteros_grandes/05_desbordamiento_y_infinito.py
```

## Conclusión personal

Python facilita los cálculos exactos con números grandes, pero eso no significa
que todos los tipos numéricos sean ilimitados. Tengo que revisar el tipo del
dato, especialmente al usar bibliotecas científicas. También debo elegir la
operación adecuada: `pow()` con módulo evita trabajo innecesario, `isqrt()`
mantiene el cálculo entero e infinito solo sirve como valor especial de `float`.

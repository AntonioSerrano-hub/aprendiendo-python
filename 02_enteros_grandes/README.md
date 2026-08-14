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

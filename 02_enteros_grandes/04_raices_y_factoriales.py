"""Cuarta práctica: trabajar de forma exacta con isqrt() y factorial()."""

import math


def es_cuadrado_perfecto(numero: int) -> bool:
    """Indica si un entero no negativo tiene una raíz cuadrada exacta."""
    if numero < 0:
        return False

    raiz = math.isqrt(numero)
    return raiz * raiz == numero


def contar_ordenes_posibles(cantidad_tareas: int) -> tuple[int, int]:
    """Devuelve las permutaciones de tareas y la cantidad de dígitos."""
    if cantidad_tareas < 0:
        raise ValueError("La cantidad de tareas no puede ser negativa")

    posibilidades = math.factorial(cantidad_tareas)
    return posibilidades, len(str(posibilidades))


def main() -> None:
    """Prueba raíces exactas y muestra cuánto crece un factorial."""
    mediciones = [81, 82, 10**100]

    for medicion in mediciones:
        raiz = math.isqrt(medicion)
        print(f"¿{medicion} es cuadrado perfecto? {es_cuadrado_perfecto(medicion)}")
        print(f"Raíz entera: {raiz}\n")

    posibilidades, cantidad_digitos = contar_ordenes_posibles(1000)
    print(f"Formas de ordenar 1000 tareas: {cantidad_digitos} dígitos")
    print(f"Primeros 20 dígitos: {str(posibilidades)[:20]}...")


if __name__ == "__main__":
    main()

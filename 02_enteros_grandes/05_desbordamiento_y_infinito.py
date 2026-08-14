"""Quinta práctica: comparar int con 8 bits y revisar float('inf')."""

import ctypes
import math


def comparar_suma() -> None:
    """Compara la misma suma con un int de Python y otro de 8 bits."""
    valor = 127
    resultado_python = valor + 1
    resultado_int8 = ctypes.c_int8(valor + 1).value

    print("Suma de 127 + 1")
    print(f"int de Python: {resultado_python}")
    print(f"entero de 8 bits: {resultado_int8}")
    print("El entero de 8 bits vuelve a -128 porque solamente guarda 256 valores.")


def revisar_infinito() -> None:
    """Comprueba que infinito es un float y no sirve donde se exige un int."""
    infinito = float("inf")

    print(f"\nTipo de infinito: {type(infinito).__name__}")
    print(f"¿Infinito es mayor que 10**100? {infinito > 10**100}")

    try:
        math.isqrt(infinito)
    except TypeError as error:
        print(f"math.isqrt(infinito) falla: {error}")


def main() -> None:
    """Ejecuta las dos comparaciones de la práctica."""
    comparar_suma()
    revisar_infinito()


if __name__ == "__main__":
    main()

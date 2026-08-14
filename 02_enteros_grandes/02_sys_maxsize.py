"""Segunda práctica: diferenciar sys.maxsize del máximo de un int."""

import sys


def main() -> None:
    """Supera sys.maxsize para comprobar que la suma sigue siendo exacta."""
    limite_indice = sys.maxsize
    numero_mayor = limite_indice + 1
    numero_mucho_mayor = limite_indice**2

    print(f"sys.maxsize: {limite_indice}")
    print(f"sys.maxsize + 1: {numero_mayor}")
    print(f"sys.maxsize al cuadrado: {numero_mucho_mayor}")
    print(f"Tipo del resultado: {type(numero_mucho_mayor).__name__}")

    assert numero_mayor > sys.maxsize
    print("\nEl cálculo funciona: sys.maxsize no es el máximo entero de Python.")
    print("Representa un límite práctico para índices y tamaños de colecciones.")


if __name__ == "__main__":
    main()

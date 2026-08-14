"""Primera práctica: comprobar que los enteros de Python pueden crecer."""

import sys


def mostrar_crecimiento(numero: int) -> None:
    """Muestra el tamaño lógico y el espacio ocupado por un entero."""
    print(f"Valor: {numero}")
    print(f"Cantidad de bits: {numero.bit_length()}")
    print(f"Memoria aproximada: {sys.getsizeof(numero)} bytes")
    print("-" * 50)


def main() -> None:
    """Compara enteros chicos con otros que superan los 64 bits."""
    numeros = [25, 2**63 - 1, 2**63, 2**100, 10**100]

    for numero in numeros:
        mostrar_crecimiento(numero)

    print("Conclusión: el valor crece y Python reserva más memoria cuando hace falta.")


if __name__ == "__main__":
    main()

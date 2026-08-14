"""Tercera práctica: usar pow() con módulo sin crear un número gigante."""


def calcular_codigo_equipo(numero_serie: int) -> int:
    """Genera un código corto a partir de un número de serie positivo."""
    if numero_serie <= 0:
        raise ValueError("El número de serie debe ser positivo")

    # El tercer argumento hace la potencia y el módulo en una sola operación.
    return pow(7, numero_serie, 97)


def main() -> None:
    """Calcula códigos incluso cuando el exponente es muy grande."""
    numeros_serie = [12, 250, 10_000_000]

    for numero_serie in numeros_serie:
        codigo = calcular_codigo_equipo(numero_serie)
        print(f"Equipo {numero_serie:>10}: código {codigo:02d}")

    ejemplo_chico = 12
    assert pow(7, ejemplo_chico, 97) == (7**ejemplo_chico) % 97
    print("\nPara un caso chico verifiqué que ambas formas dan el mismo resultado.")


if __name__ == "__main__":
    main()

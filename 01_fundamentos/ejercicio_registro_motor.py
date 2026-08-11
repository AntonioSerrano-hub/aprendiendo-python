"""Ejercicio práctico para reconocer y convertir tipos de datos en Python."""


def crear_registro_motor(
    nombre: str,
    potencia_kw: float,
    temperaturas: list[float],
    esta_encendido: bool,
) -> dict[str, object]:
    """Crea un registro y calcula la temperatura promedio del motor."""
    temperatura_promedio = sum(temperaturas) / len(temperaturas)

    return {
        "nombre": nombre,
        "potencia_kw": potencia_kw,
        "temperaturas_c": temperaturas,
        "temperatura_promedio_c": round(temperatura_promedio, 2),
        "esta_encendido": esta_encendido,
        "datos_nominales": (380, 50),
        "alarmas": {"temperatura_alta"} if temperatura_promedio > 80 else set(),
    }


def mostrar_registro(registro: dict[str, object]) -> None:
    """Imprime el contenido y el tipo de cada dato del registro."""
    print("\nRegistro del motor")
    print("-" * 40)
    for clave, valor in registro.items():
        print(f"{clave}: {valor!r} -> {type(valor).__name__}")


def main() -> None:
    """Solicita datos, realiza conversiones y muestra el resultado."""
    nombre = input("Nombre del motor: ").strip() or "Motor principal"
    potencia_kw = float(input("Potencia en kW: "))
    temperaturas = [72.5, 78.2, 81.0]
    esta_encendido = input("¿Está encendido? (s/n): ").strip().lower() == "s"

    registro = crear_registro_motor(
        nombre,
        potencia_kw,
        temperaturas,
        esta_encendido,
    )
    mostrar_registro(registro)


if __name__ == "__main__":
    main()

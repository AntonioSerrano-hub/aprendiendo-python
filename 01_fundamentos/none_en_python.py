"""Ejemplo práctico del uso de None en un registro de temperaturas."""


def obtener_temperatura(sensor_id: str) -> float | None:
    """Devuelve la temperatura registrada o None si no hay una medición."""
    temperaturas = {
        "motor_principal": 72.5,
        "motor_reserva": None,
    }
    return temperaturas.get(sensor_id)


def crear_mensaje(
    sensor_id: str,
    observacion: str | None = None,
) -> str:
    """Crea un mensaje y controla primero los valores ausentes."""
    temperatura = obtener_temperatura(sensor_id)

    # Esta condición evita operar con None como si fuera un número.
    if temperatura is None:
        return f"{sensor_id}: no hay una medición disponible"

    estado = "alta" if temperatura > 80 else "normal"

    if observacion is None:
        observacion = "sin observaciones"

    return (
        f"{sensor_id}: {temperatura} °C, estado {estado}, "
        f"{observacion}"
    )


def comparar_valores_vacios() -> None:
    """Demuestra que None, cero y una cadena vacía no significan lo mismo."""
    valores = [None, 0, ""]

    print("\nComparación de valores:")
    for valor in valores:
        print(f"{valor!r:>4} -> ¿es None? {valor is None}")


def main() -> None:
    """Ejecuta varios casos para practicar el comportamiento de None."""
    print(crear_mensaje("motor_principal", "equipo en servicio"))
    print(crear_mensaje("motor_reserva"))
    print(crear_mensaje("sensor_inexistente"))
    comparar_valores_vacios()


if __name__ == "__main__":
    main()

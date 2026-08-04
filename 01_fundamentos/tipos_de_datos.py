"""Ejemplos de tipos de datos aplicados a ingeniería electromecánica."""


def mostrar_datos_motor() -> None:
    """Muestra datos básicos y mediciones de un motor eléctrico."""
    nombre_motor = "Motor principal"
    potencia_kw = 15
    temperatura_c = 72.5
    motor_encendido = True

    mediciones_temperatura = [70.2, 71.5, 72.5]
    datos_nominales = (380, 50)
    estados_registrados = {"marcha", "detenido", "marcha"}

    motor = {
        "nombre": nombre_motor,
        "potencia_kw": potencia_kw,
        "temperatura_c": temperatura_c,
        "encendido": motor_encendido,
    }

    print(f"Motor: {motor['nombre']}")
    print(f"Potencia: {motor['potencia_kw']} kW")
    print(f"Temperatura actual: {motor['temperatura_c']} °C")
    print(f"Encendido: {motor['encendido']}")
    print(f"Mediciones: {mediciones_temperatura}")
    print(f"Tensión y frecuencia nominal: {datos_nominales}")
    print(f"Estados sin duplicados: {estados_registrados}")


if __name__ == "__main__":
    mostrar_datos_motor()


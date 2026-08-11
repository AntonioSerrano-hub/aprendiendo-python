# Fundamentos de Python

## Tipos de datos principales

Cada valor de Python tiene un tipo. El tipo determina qué información contiene
y qué operaciones se pueden realizar con ella.

| Tipo | Ejemplo | Uso habitual |
| --- | --- | --- |
| `int` | `15` | Números enteros |
| `float` | `72.5` | Números con decimales |
| `complex` | `10 + 3j` | Números complejos |
| `str` | `"Motor principal"` | Texto |
| `bool` | `True` | Estados lógicos |
| `list` | `[70.2, 71.5]` | Colección ordenada y modificable |
| `tuple` | `(380, 50)` | Colección ordenada e inmutable |
| `set` | `{"alarma", "marcha"}` | Elementos sin duplicados |
| `dict` | `{"potencia_kw": 15}` | Información en pares clave-valor |

## Ideas importantes

- `input()` devuelve texto, aunque el usuario escriba un número.
- `int()` y `float()` permiten convertir texto en valores numéricos.
- Las listas pueden modificarse; las tuplas no.
- Los conjuntos eliminan valores duplicados.
- Los diccionarios permiten representar equipos y mediciones con claridad.
- `type(valor)` muestra el tipo de un valor.

El archivo `tipos_de_datos.py` contiene ejemplos ejecutables y una aplicación
sencilla relacionada con un motor eléctrico.

## Valores ausentes con `None`

`None` representa la ausencia de un valor. No es igual a `0`, `False` ni una
cadena vacía. La forma recomendada de comprobarlo es con `is None` o
`is not None`.

El archivo `none_en_python.py` utiliza mediciones de sensores para mostrar:

- Una función que puede devolver un número o `None`.
- Un parámetro opcional cuyo valor inicial es `None`.
- Una cláusula de guarda que evita operar con una medición ausente.
- La diferencia entre `None`, cero y una cadena vacía.

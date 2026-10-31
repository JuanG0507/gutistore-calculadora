"""Calculadora de compras por consola para GUTISTORE."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENTAVO = Decimal("0.01")


def pedir_texto(mensaje: str) -> str:
    """Solicita un texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")


def pedir_decimal(mensaje: str, minimo: Decimal, maximo: Decimal | None = None) -> Decimal:
    """Solicita un número decimal dentro del rango permitido."""
    while True:
        try:
            valor = Decimal(input(mensaje).strip().replace(",", "."))
            if not valor.is_finite():
                raise InvalidOperation
            if valor < minimo or (maximo is not None and valor > maximo):
                rango = f"mayor o igual a {minimo}"
                if maximo is not None:
                    rango += f" y menor o igual a {maximo}"
                print(f"El valor debe ser {rango}.")
                continue
            return valor
        except (InvalidOperation, ValueError):
            print("Ingresa un número válido.")


def pedir_cantidad() -> int:
    """Solicita una cantidad entera positiva."""
    while True:
        cantidad = pedir_decimal("Cantidad: ", Decimal("1"))
        if cantidad == cantidad.to_integral_value():
            return int(cantidad)
        print("La cantidad debe ser un número entero.")


def calcular_compra(precio: Decimal, cantidad: int, descuento_porcentaje: Decimal) -> tuple[Decimal, Decimal, Decimal]:
    """Devuelve subtotal, descuento y total, redondeados a dos decimales."""
    subtotal = (precio * cantidad).quantize(CENTAVO, rounding=ROUND_HALF_UP)
    descuento = (subtotal * descuento_porcentaje / 100).quantize(CENTAVO, rounding=ROUND_HALF_UP)
    total = (subtotal - descuento).quantize(CENTAVO, rounding=ROUND_HALF_UP)
    return subtotal, descuento, total


def main() -> None:
    print("=" * 32)
    print("       GUTISTORE | Compras")
    print("=" * 32)

    producto = pedir_texto("Producto: ")
    precio = pedir_decimal("Precio por unidad (COP): $", Decimal("0.01"))
    cantidad = pedir_cantidad()
    descuento_porcentaje = pedir_decimal("Descuento (0-100 %): ", Decimal("0"), Decimal("100"))

    subtotal, descuento, total = calcular_compra(precio, cantidad, descuento_porcentaje)

    print("\n" + "-" * 32)
    print(f"Producto:             {producto}")
    print(f"Precio por unidad:    ${precio:,.2f} COP")
    print(f"Cantidad:             {cantidad}")
    print(f"Subtotal:             ${subtotal:,.2f} COP")
    print(f"Descuento ({descuento_porcentaje}%):   -${descuento:,.2f} COP")
    print(f"Total a pagar:        ${total:,.2f} COP")
    print("-" * 32)


if __name__ == "__main__":
    main()

# GUTISTORE | Calculadora de compras

Aplicación de consola escrita en Python para calcular el valor de una compra, aplicar un descuento y mostrar el total a pagar en pesos colombianos (COP).

## Funcionalidades

- Solicita el nombre del producto, su precio y la cantidad.
- Aplica un descuento entre 0 % y 100 %.
- Valida los datos ingresados y permite usar coma o punto decimal.
- Calcula valores monetarios con `Decimal` y redondea a dos decimales.
- Muestra el subtotal, el descuento y el total.

## Requisitos

- Python 3.10 o superior.
- No requiere dependencias externas.

## Uso

```bash
python Compra.py
```

Ejemplo de interacción:

```text
================================
       GUTISTORE | Compras
================================
Producto: Camiseta
Precio por unidad (COP): $45000
Cantidad: 2
Descuento (0-100 %): 10

--------------------------------
Producto:             Camiseta
Precio por unidad:    $45,000.00 COP
Cantidad:             2
Subtotal:             $90,000.00 COP
Descuento (10%):      -$9,000.00 COP
Total a pagar:        $81,000.00 COP
--------------------------------
```

## Estructura

```text
.
├── Compra.py       # Aplicación de consola
├── README.md       # Descripción e instrucciones
├── LICENSE         # Licencia MIT
└── .gitignore      # Archivos locales excluidos de Git
```

## Aprendizajes demostrados

Este proyecto practica entrada y validación de datos, funciones, control de flujo, manejo de errores y operaciones monetarias con `Decimal` en Python.

## Autor

Juan José Gutiérrez — [@JuanG0507](https://github.com/JuanG0507)

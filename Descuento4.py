"""
Programa 4: Cálculo de precio con descuento.
Calcula el descuento aplicable y el precio final de un producto
según su precio original.
"""

def main():
    # Constantes de descuento
    DESC_10 = 0.10
    DESC_20 = 0.20
    DESC_25 = 0.25

    # Entrada de datos
    precio_original = float(input("Ingrese el precio del producto: $"))

    # Proceso y Validación
    if precio_original <= 0:
        print("\nError: El precio ingresado debe ser mayor a 0.")
    elif precio_original <= 100:
        descuento = 0.0
        porcentaje_texto = "0%"
    elif precio_original <= 200:
        descuento = precio_original * DESC_10
        porcentaje_texto = "10%"
    elif precio_original <= 500:
        descuento = precio_original * DESC_20
        porcentaje_texto = "20%"
    else:
        descuento = precio_original * DESC_25
        porcentaje_texto = "25%"

    # Salida (solo si el precio fue válido)
    if precio_original > 0:
        precio_final = precio_original - descuento
        print(f"\nPrecio original: ${precio_original:.2f}")
        print(f"Descuento aplicado ({porcentaje_texto}): ${descuento:.2f}")
        print(f"Precio final a pagar: ${precio_final:.2f}")

if __name__ == "__main__":
    main()
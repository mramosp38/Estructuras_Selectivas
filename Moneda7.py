"""
Programa 7: Conversor de monedas.
Convierte un monto en pesos mexicanos (MXN) a 10 diferentes monedas extranjeras
utilizando la estructura match-case.
"""

def main():
    # Constantes: Tasa de cambio de 1 moneda extranjera expresada en Pesos Mexicanos (MXN)
    TASA_USD = 18.00    # Dólar estadounidense
    TASA_EUR = 19.50    # Euro
    TASA_THB = 0.52     # Baht tailandés
    TASA_JPY = 0.12     # Yen japonés
    TASA_KRW = 0.013    # Won surcoreano
    TASA_AUD = 12.10    # Dólar australiano
    TASA_PEN = 4.80     # Sol peruano
    TASA_CAD = 13.20    # Dólar canadiense
    TASA_VES = 0.45     # Bolívar venezolano
    TASA_ARS = 0.018    # Peso argentino

    # Entrada de datos y validación
    pesos = float(input("Ingrese la cantidad en pesos mexicanos (MXN): $"))

    if pesos <= 0:
        print("\nError: La cantidad de pesos debe ser mayor a cero.")
    else:
        # Menú de opciones
        print("\n--- SELECCIONE LA MONEDA A CONVERTIR ---")
        print("1. Dólar (USD)")
        print("2. Euro (EUR)")
        print("3. Baht (THB)")
        print("4. Yen (JPY)")
        print("5. Won (KRW)")
        print("6. Dólar Australiano (AUD)")
        print("7. Sol (PEN)")
        print("8. Dólar Canadiense (CAD)")
        print("9. Bolívar (VES)")
        print("10. Peso Argentino (ARS)")

        opcion = int(input("\nElija una opción (1-10): "))

        # Conversión con match-case
        match opcion:
            case 1:
                resultado = pesos / TASA_USD
                print(f"\n${pesos:.2f} MXN equivalen a: ${resultado:.2f} USD")
            case 2:
                resultado = pesos / TASA_EUR
                print(f"\n${pesos:.2f} MXN equivalen a: €{resultado:.2f} EUR")
            case 3:
                resultado = pesos / TASA_THB
                print(f"\n${pesos:.2f} MXN equivalen a: ฿{resultado:.2f} THB")
            case 4:
                resultado = pesos / TASA_JPY
                print(f"\n${pesos:.2f} MXN equivalen a: ¥{resultado:.2f} JPY")
            case 5:
                resultado = pesos / TASA_KRW
                print(f"\n${pesos:.2f} MXN equivalen a: ₩{resultado:.2f} KRW")
            case 6:
                resultado = pesos / TASA_AUD
                print(f"\n${pesos:.2f} MXN equivalen a: ${resultado:.2f} AUD")
            case 7:
                resultado = pesos / TASA_PEN
                print(f"\n${pesos:.2f} MXN equivalen a: S/{resultado:.2f} PEN")
            case 8:
                resultado = pesos / TASA_CAD
                print(f"\n${pesos:.2f} MXN equivalen a: ${resultado:.2f} CAD")
            case 9:
                resultado = pesos / TASA_VES
                print(f"\n${pesos:.2f} MXN equivalen a: Bs.{resultado:.2f} VES")
            case 10:
                resultado = pesos / TASA_ARS
                print(f"\n${pesos:.2f} MXN equivalen a: ${resultado:.2f} ARS")
            case _:
                print("\nError: Opción no válida. Debe seleccionar un número del 1 al 10.")

if __name__ == "__main__":
    main()
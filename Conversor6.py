"""
Programa 6: Convertidor de grados Celsius.
Convierte una temperatura en grados Celsius a Fahrenheit o Kelvin
utilizando la estructura match-case según la opción del usuario.
"""

def main():
    # Entrada de temperatura
    celsius = float(input("Ingrese la temperatura en grados Celsius (°C): "))

    # Mostrar menú de opciones
    print("\n--- MENÚ DE CONVERSIÓN ---")
    print("1. Convertir a Fahrenheit (°F)")
    print("2. Convertir a Kelvin (K)")
    
    opcion = int(input("Seleccione una opción (1 o 2): "))

    # Proceso y Salida con match-case
    match opcion:
        case 1:
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"\n{celsius}°C equivalen a {fahrenheit:.2f}°F")
        case 2:
            kelvin = celsius + 273.15
            print(f"\n{celsius}°C equivalen a {kelvin:.2f} K")
        case _:
            print("\nError: Opción no válida. Debe seleccionar 1 o 2.")

if __name__ == "__main__":
    main()
"""
Programa 5: Determinar la estación del año.
Asigna la estación del año según el número de mes ingresado (1 al 12)
utilizando la estructura match-case.
"""

def main():
    # Entrada de datos
    mes = int(input("Ingrese el número del mes (1-12): "))

    # Evaluación con match-case
    match mes:
        case 12 | 1 | 2:
            estacion = "Invierno"
            print(f"\nEl mes {mes} pertenece a la estación: {estacion}")
        case 3 | 4 | 5:
            estacion = "Primavera"
            print(f"\nEl mes {mes} pertenece a la estación: {estacion}")
        case 6 | 7 | 8:
            estacion = "Verano"
            print(f"\nEl mes {mes} pertenece a la estación: {estacion}")
        case 9 | 10 | 11:
            estacion = "Otoño"
            print(f"\nEl mes {mes} pertenece a la estación: {estacion}")
        case _:
            print("\nError: Número de mes no válido. Debe ser un entero entre 1 y 12.")

if __name__ == "__main__":
    main()
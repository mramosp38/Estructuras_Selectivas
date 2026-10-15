"""
Programa 2: Verificar edad para votar.
Determina si una persona cumple con la edad mínima para votar (18 años)
y valida que la edad ingresada sea un valor real.
"""

def main():
    # Entrada de datos
    edad = int(input("Ingrese su edad en años: "))

    # Proceso y Validación con Estructura Selectiva
    if edad < 0 or edad > 120:
        print("\nError: Ingrese una edad válida e irrealmente posible.")
    elif edad >= 18:
        print(f"\nCon {edad} años, USTED ES ELEGIBLE para votar.")
    else:
        print(f"\nCon {edad} años, USTED NO ES ELEGIBLE para votar todavía.")

if __name__ == "__main__":
    main()
"""
Programa 3: Evaluación de calificaciones con letras.
Convierte una calificación numérica (0-100) en una letra (A, B, C, D, F)
evaluando los rangos de mayor a menor.
"""

def main():
    # Entrada de datos
    calificacion = float(input("Ingrese la calificación numérica (0-100): "))

    # Validación de rango e identificación de letra
    if calificacion < 0 or calificacion > 100:
        print("\nError: La calificación debe estar entre 0 y 100.")
    elif calificacion >= 90:
        letra = "A"
        print(f"\nCalificación: {calificacion} -> Asignación: {letra}")
    elif calificacion >= 80:
        letra = "B"
        print(f"\nCalificación: {calificacion} -> Asignación: {letra}")
    elif calificacion >= 70:
        letra = "C"
        print(f"\nCalificación: {calificacion} -> Asignación: {letra}")
    elif calificacion >= 60:
        letra = "D"
        print(f"\nCalificación: {calificacion} -> Asignación: {letra}")
    else:
        letra = "F"
        print(f"\nCalificación: {calificacion} -> Asignación: {letra}")

if __name__ == "__main__":
    main()
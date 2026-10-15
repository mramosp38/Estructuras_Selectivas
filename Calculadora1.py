"""
Programa 1: Calculadora de calificaciones finales.
Calcula el promedio ponderado de tres evaluaciones asegurando
que cada una esté dentro del rango válido (0 a 100).
"""

def main():
    # Constantes de ponderación
    PORC_PARCIALES = 0.40
    PORC_PROYECTO = 0.30
    PORC_EXAMEN = 0.30

    # Entrada de datos
    parciales = float(input("Ingrese la calificación de Parciales (0-100): "))
    proyecto = float(input("Ingrese la calificación del Proyecto (0-100): "))
    examen = float(input("Ingrese la calificación del Examen Final (0-100): "))

    # Proceso y Validación con Estructura Selectiva (if-else)
    if 0 <= parciales <= 100 and 0 <= proyecto <= 100 and 0 <= examen <= 100:
        calificacion_final = (parciales * PORC_PARCIALES) + (proyecto * PORC_PROYECTO) + (examen * PORC_EXAMEN)
        print(f"\nLa calificación final del estudiante es: {calificacion_final:.2f}")
    else:
        print("\nError: Una o más calificaciones están fuera del rango permitido (0 a 100).")

if __name__ == "__main__":
    main()
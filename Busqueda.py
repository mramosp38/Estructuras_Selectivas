"""
Programa 8: Brindar información de actores de cine.
Muestra datos relevantes sobre un actor seleccionado
utilizando la estructura match-case.
"""

def main():
    print("=== CENTRO DE INFORMACIÓN: ACTORES DE CINE ===")
    print("Opciones disponibles para consultar:")
    print("- Pedro Pascal")
    print("- Salma Hayek")
    print("- Leonardo DiCaprio")
    print("- Diego Luna")
    print("- Cillian Murphy")

    # Entrada de datos (convertimos a minúsculas y quitamos espacios extras)
    busqueda = input("\nIngrese el nombre del actor/actriz que desea consultar: ").strip().lower()

    # Evaluación con match-case
    match busqueda:
        case "pedro pascal" | "pascal":
            print("\n--- PEDRO PASCAL ---")
            print("Nacionalidad: Chileno-estadounidense")
            print("Películas/Series destacadas: The Mandalorian, The Last of Us, Gladiator II.")
            print("Reconocimientos: Nominado al Emmy y Globo de Oro.")
        case "salma hayek" | "salma":
            print("\n--- SALMA HAYEK ---")
            print("Nacionalidad: Mexicana")
            print("Películas destacadas: Frida, Desperado, Eternals, House of Gucci.")
            print("Reconocimientos: Nominada al Óscar como Mejor Actriz por 'Frida'.")
        case "leonardo dicaprio" | "dicaprio":
            print("\n--- LEONARDO DICAPRIO ---")
            print("Nacionalidad: Estadounidense")
            print("Películas destacadas: Titanic, Inception, The Wolf of Wall Street, The Revenant.")
            print("Reconocimientos: Ganador del Premio Óscar a Mejor Actor en 2016.")
        case "diego luna" | "diego":
            print("\n--- DIEGO LUNA ---")
            print("Nacionalidad: Mexicana")
            print("Películas/Series destacadas: Y tu mamá también, Rogue One, Andor.")
            print("Reconocimientos: Nominado al Globo de Oro por su rol en 'Andor'.")
        case "cillian murphy" | "cillian":
            print("\n--- CILLIAN MURPHY ---")
            print("Nacionalidad: Irlandés")
            print("Películas/Series destacadas: Oppenheimer, Peaky Blinders, Inception, The Dark Knight.")
            print("Reconocimientos: Ganador del Premio Óscar a Mejor Actor por 'Oppenheimer'.")
        case _:
            print("\nError: El actor o actriz ingresado no se encuentra en la base de datos.")

if __name__ == "__main__":
    main()
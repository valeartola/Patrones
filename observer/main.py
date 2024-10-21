from observer import Libro, Biblioteca

def main():
    # Crear un libro con título y estado "MALO"
    libro = Libro("Windows es estable", "MALO")

    # Crear una instancia de la biblioteca y devolver el libro
    biblioteca = Biblioteca()
    biblioteca.devuelve_libro(libro)

if __name__ == "__main__":
    main()

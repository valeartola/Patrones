from triangulo import *

def main():
    factory = TrianguloFactory()
    triangulo = factory.create_triangulo(20, 30, 10)
    print(triangulo.getDescripcion())

if __name__ == "__main__":
    main()
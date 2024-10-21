from abc import ABC, abstractmethod
import math

class Triangulo(ABC):
    def __init__(self,ladoA, ladoB, ladoC ):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    @abstractmethod
    def getDescripcion(self):
        pass

    @abstractmethod
    def getSuperficie(self):
        pass

    @abstractmethod
    def dibujate(self):
        pass

    def getLadoA(self):
        return self.ladoA
    
    def set_ladoA(self, valor):
        self._ladoA = valor
    
    def getLadoB(self):
        return self.ladoB
    
    def set_ladoB(self, valor):
        self.ladoB = valor

    def getLadoC(self):
        return self.ladoC
    
    def set_ladoC(self, valor):       
        self._ladoC = valor      

class Equilatero(Triangulo):
    
    def getDescripcion(self):
        return 'Soy un Triangulo Equilátero'
    
    def getSuperficie(self):
        return (math.sqrt(3) / 4) * (self._ladoA ** 2)

    def dibujate(self):
        altura = self._ladoA
        for i in range(1, altura + 1):
            espacios = ' ' * (altura - i)
            asteriscos = '*' * (2 * i - 1)
            print(espacios + asteriscos)

class Escaleno(Triangulo):
   
    def getDescripcion(self):
        return "Soy un Triángulo Escaleno"

    def getSuperficie(self):
        s = (self._ladoA + self._ladoB + self._ladoC) / 2
        return math.sqrt(s * (s - self._ladoA) * (s - self._ladoB) * (s - self._ladoC))

    def dibujate(self):
        print("Dibujando un triángulo escaleno (representación simple):")
        print("    *")
        print("   * *")
        print("  *   *")
        print(" *     *")
        print("*********")

class Isosceles(Triangulo):
    
    def getDescripcion(self):
        return "Soy un Triángulo Isosceles"

    def getSuperficie(self):
        s = (self._ladoA + self._ladoB + self._ladoC) / 2
        return math.sqrt(s * (s - self._ladoA) * (s - self._ladoB) * (s - self._ladoC))

    def dibujate(self):
        print("Dibujando un triángulo escaleno (representación simple):")
        print("    *")
        print("   * *")
        print("  *   *")
        print(" *     *")
        print("********")


class TrianguloFactoryMethod(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC):
        pass

class TrianguloFactoryBase(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC) -> Triangulo:
        pass

class TrianguloFactory(TrianguloFactoryMethod):
    def create_triangulo(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)
        


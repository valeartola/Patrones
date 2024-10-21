from abc import ABC, abstractmethod
import copy

class TV(ABC):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0):
        self._marca = marca
        self._pulgadas = pulgadas
        self._color = color
        self._descripcion = ""
        self._precio = precio

    def clone(self):
        return copy.deepcopy(self)

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_pulgadas(self):
        return self._pulgadas

    def set_pulgadas(self, pulgadas):
        self._pulgadas = pulgadas

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
# Clase abstracta Color
class Color(ABC):
    def __init__(self):
        self._descripcion = ""

    @abstractmethod
    def colorea(self, tv):
        pass

    def get_descripcion(self):
        return self._descripcion

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

class TvAbstractFactory(ABC):
    @abstractmethod
    def create_color(self) -> Color:
        pass

    @abstractmethod
    def create_tv(self) -> TV:
        pass
    
class Amarillo(Color):
    def __init__(self):
        super().__init__()
        self._es_primario = True

    def colorea(self, tv):
        print(f"Pintando de amarillo el {tv.get_descripcion()}")

    def is_es_primario(self):
        return self._es_primario

    def set_es_primario(self, es_primario):
        self._es_primario = es_primario

class Azul(Color):
    def __init__(self):
        super().__init__()
        self._es_primario = True

    def colorea(self, tv):
        print(f"Pintando de azul el {tv.get_descripcion()}")

    def is_es_primario(self):
        return self._es_primario

    def set_es_primario(self, es_primario):
        self._es_primario = es_primario

class LCD(TV):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0, costo_fabricacion=0.0):
        super().__init__(marca, pulgadas, color, precio)
        self._costo_fabricacion = costo_fabricacion
        self.set_descripcion("LCD")

    def get_costo_fabricacion(self):
        return self._costo_fabricacion

    def set_costo_fabricacion(self, costo_fabricacion):
        self._costo_fabricacion = costo_fabricacion

class Plasma(TV):
    def __init__(self, marca="", pulgadas=0, color="", precio=0.0, angulo_vision=0.0, tiempo_respuesta=0.0):
        super().__init__(marca, pulgadas, color, precio)
        self._angulo_vision = angulo_vision
        self._tiempo_respuesta = tiempo_respuesta
        self.set_descripcion("Plasma... próximamente será un LED")

    def get_angulo_vision(self):
        return self._angulo_vision

    def set_angulo_vision(self, angulo_vision):
        self._angulo_vision = angulo_vision

    def get_tiempo_respuesta(self):
        return self._tiempo_respuesta

    def set_tiempo_respuesta(self, tiempo_respuesta):
        self._tiempo_respuesta = tiempo_respuesta

class FactoryLcdAzul(TvAbstractFactory):
    def create_color(self):
        return Azul()

    def create_tv(self):
        return LCD()
    
class FactoryPlasmaAmarillo(TvAbstractFactory):
    def create_color(self):
        return Amarillo()

    def create_tv(self):
        return Plasma()
    

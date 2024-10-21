from abc import ABC, abstractmethod

class Libro:
    def __init__(self, titulo, estado):
        self._titulo = titulo
        self._estado = estado

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

class ILibroMalEstado(ABC):
    @abstractmethod
    def update(self):
        pass

class Biblioteca:
    def devuelve_libro(self, libro):
        if libro.get_estado() == "MALO":
            alarma = AlarmaLibro()
            alarma.add_observer(Compras())
            alarma.add_observer(Administracion())
            alarma.add_observer(Stock())
            alarma.dispara_alarma(libro)

class Administracion(ILibroMalEstado):
    def update(self,mensaje):
        print(f"Administración: {mensaje}")
        print("Envio una queja formal...")

class Compras(ILibroMalEstado):
    def update(self, mensaje):
        print(f"Compras: {mensaje}")
        print("Solicito nueva cotización...")

class AlarmaLibro:
    def __init__(self):
        self._observadores = []

    def add_observer(self, observador):
        self._observadores.append(observador)

    def remove_observer(self, observador):
        self._observadores.remove(observador)

    def notify_observers(self, mensaje):
        for observador in self._observadores:
            observador.update(mensaje)

    def dispara_alarma(self, libro):
        mensaje = f"Rompieron el libro, {libro.get_titulo()}"
        print(mensaje)
        self.notify_observers(mensaje)

class Stock(ILibroMalEstado):
    def update(self,mensaje):
        print("Stock: ", mensaje)
        print("Le doy de baja...")

class Subject(ABC):
    @abstractmethod
    def attach(self, observador: ILibroMalEstado):
        pass

    @abstractmethod
    def detach(self, observador: ILibroMalEstado):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


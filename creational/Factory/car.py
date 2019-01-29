from abc import ABC,abstractmethod

class Car(ABC):
    """docstring for Car"""

    @abstractmethod # not necessary
    def get_label(self):
        pass
    
    @abstractmethod # not necessary
    def get_transmision(self):
        pass

    @abstractmethod # not necessary
    def get_engine_power(self):
        pass

    def get_class_name(self):
        return self.__module__.capitalize()

    def __str__(self):
        return "Car %s [get_label()=%s, get_transmition()=%s,get_engine_power()=%s]" % (
            self.get_class_name(),
            self.get_label(),
            self.get_transmision(),
            self.get_engine_power()
        )



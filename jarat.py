from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def get_tipus(self):
        pass

class BelfoldiJarat(Jarat):
    def get_tipus(self):
        return "Belföldi"

class NemzetkoziJarat(Jarat):
    def get_tipus(self):
        return "Nemzetközi"

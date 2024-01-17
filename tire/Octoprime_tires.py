import typing
from tire.tire import Tire

class Octoprime_tires(Tire):
    """ Carrigan tires"""
    def __init__(self, tire_wear: list[float]):
        self.tire_wear = tire_wear
    
    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
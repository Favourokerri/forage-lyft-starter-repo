from .CarFactory import CarFactory
from ..battery.NubbinBattery import NubbinBattery
from ..engine.capulet_engine import CapuletEngine
from car import Car
from datetime import timedelta, date

class create_rorschach(CarFactory):
    def create_car(self, current_date: date, last_service_date, last_service_mileage: int, current_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
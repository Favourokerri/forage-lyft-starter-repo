from .CarFactory import CarFactory
from battery.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from car import Car
from datetime import timedelta, date

class create_calliope(CarFactory):
    def create_car(self, current_date: date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
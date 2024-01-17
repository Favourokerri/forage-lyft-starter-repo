from .CarFactory import CarFactory
from battery.SpindlerBattery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from datetime import timedelta, date

class create_glissade(CarFactory):
    def create_car(self, current_date: date, last_service_date, last_service_mileage: int, current_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
from .CarFactory import CarFactory
from battery.SpindlerBattery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from car import Car
from datetime import timedelta, date

class create_palindrome(CarFactory):
    def create_car(self, current_date: date, last_service_date: int, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
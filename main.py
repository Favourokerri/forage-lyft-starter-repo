from carfactory.CarFactory import CarFactory 
from datetime import datetime, date
from carfactory.CalliopeCarFactory import create_calliope
from carfactory.create_palindrome import create_palindrome

car1 = create_calliope()
today = date.today()
last_service_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
calliope = car1.create_car(current_date=today, last_service_date=last_service_date, last_service_mileage=5000, current_mileage=1000)

print(f"Calliope Car needs service: {calliope.needs_service()}")

car2 = create_palindrome()
palindrome = car2.create_car(current_date=today, last_service_date=last_service_date, warning_light_on=True)
print(f"Calliope Car2 needs service: {palindrome.needs_service()}")
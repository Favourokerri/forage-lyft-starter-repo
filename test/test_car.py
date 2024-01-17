import unittest
from datetime import datetime
from carfactory.CalliopeCarFactory import create_calliope
from carfactory.GlissadeCarFactory import create_glissade
from carfactory.create_palindrome import create_palindrome
from carfactory.create_rorschach import create_rorschach
from carfactory.throvex import create_throvex

class TestCalliope(unittest.TestCase):
    """Unit test for calliope car"""
    def test_battery_should_be_serviced(self):
        """Function to test if the battery needs to be serviced"""
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        calliope = create_calliope()
        car = calliope.create_car(today, last_service_date, current_mileage, last_service_mileage)

        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        """Testing for battery should not be serviced"""
        today = datetime.today().date()
        last_service_date2 = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        calliope = create_calliope()
        car = calliope.create_car(today, last_service_date2, current_mileage, last_service_mileage)

        self.assertFalse(car.needs_service())

    
    def test_engine_should_be_serviced(self):
        """Testing for engine"""
        today = datetime.today().date()
        last_service_date2 = today.replace(year=today.year - 1)
        current_mileage = 30001
        last_service_mileage = 0

        calliope = create_calliope()
        car = calliope.create_car(today, last_service_date2, current_mileage, last_service_mileage)
        
        self.assertTrue(car.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        """Testing for engine"""
        today = datetime.today().date()
        last_service_date2 = today.replace(year=today.year - 1)
        current_mileage = 2000
        last_service_mileage = 0

        calliope = create_calliope()
        car = calliope.create_car(today, last_service_date2, current_mileage, last_service_mileage)
        
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    """ test for glissade """
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        glissade = create_glissade()
        car = glissade.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        glissade = create_glissade()
        car = glissade.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())
    
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        glissade = create_glissade()
        car = glissade.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())


    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 30000

        glissade = create_glissade()
        car = glissade.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        palindrome = create_palindrome()
        car = palindrome.create_car(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        palindrome = create_palindrome()
        car = palindrome.create_car(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = True

        palindrome = create_palindrome()
        car = palindrome.create_car(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        palindrome = create_palindrome()
        car = palindrome.create_car(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = create_rorschach()
        car = rorschach.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = create_rorschach()
        car = rorschach.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60003
        last_service_mileage = 0

        rorschach = create_rorschach()
        car = rorschach.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60003
        last_service_mileage = 10000

        rorschach = create_rorschach()
        car = rorschach.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        throvex = create_throvex()
        car = throvex.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        throvex = create_throvex()
        car = throvex.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30004
        last_service_mileage = 0

        throvex = create_throvex()
        car = throvex.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 10000
        last_service_mileage = 0

        throvex = create_throvex()
        car = throvex.create_car(today, last_service_date, last_service_mileage, current_mileage)

        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()

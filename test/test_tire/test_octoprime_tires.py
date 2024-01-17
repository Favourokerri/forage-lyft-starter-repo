import unittest
from tire.Octoprime_tires import Octoprime_tires


class TestOctoprime_tires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.85, 0.92, 0.88, 0.95, 2]
        car_tire = Octoprime_tires(tire_wear)
        self.assertTrue(car_tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.1, 0.0, 0.1, 0.0]
        car_tire = Octoprime_tires(tire_wear)
        self.assertFalse(car_tire.needs_service())
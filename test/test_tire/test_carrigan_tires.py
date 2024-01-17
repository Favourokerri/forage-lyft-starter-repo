import unittest
from datetime import date

from tire.Carrigan_tires import Carrigan_tires


class TestCarrigan_tires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.85, 0.92, 0.88, 0.95]
        car_tire = Carrigan_tires(tire_wear)
        self.assertTrue(car_tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.5, 0.1, 0.8, 0.1]
        car_tire = Carrigan_tires(tire_wear)
        self.assertFalse(car_tire.needs_service())
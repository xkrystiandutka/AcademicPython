import unittest
from Testy_Jednostkowe_Task2 import Car, Truck, PoliceCar

class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(fuel_capacity=100, cargo_capacity=500)

    def test_load_cargo(self):
        self.truck.load_cargo(200)
        self.assertEqual(self.truck.current_cargo, 200)

    def test_load_exceeds_capacity(self):
        self.truck.load_cargo(600)
        self.assertEqual(self.truck.current_cargo, 0)

    def test_unload_cargo(self):
        self.truck.load_cargo(300)
        self.truck.unload_cargo(150)
        self.assertEqual(self.truck.current_cargo, 150)


class TestPoliceCar(unittest.TestCase):
    def setUp(self):
        self.police_car = PoliceCar()

    def test_turn_on_siren(self):
        self.police_car.turn_on_siren()
        self.assertTrue(self.police_car.is_siren_on())

    def test_turn_off_siren(self):
        self.police_car.turn_on_siren()
        self.police_car.turn_off_siren()
        self.assertFalse(self.police_car.is_siren_on())

    def test_siren_initial_state(self):
        self.assertFalse(self.police_car.is_siren_on())


if __name__ == '__main__':
    unittest.main()

import unittest
from Testy_Jednostkowe_Task1 import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()

    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)

    def test_accelerate_increases_speed(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_accelerate_decreases_fuel_level(self):
        initial_fuel_level = self.car.fuel_level
        self.car.accelerate()
        self.assertLess(self.car.fuel_level, initial_fuel_level)

    def test_brake_decreases_speed(self):
        self.car.accelerate()
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_step_increases_odometer(self):
        initial_odometer = self.car.odometer
        self.car.accelerate()
        self.car.step()
        self.assertGreater(self.car.odometer, initial_odometer)

    def test_step_decreases_fuel_level(self):
        initial_fuel_level = self.car.fuel_level
        self.car.accelerate()
        self.car.step()
        self.assertLess(self.car.fuel_level, initial_fuel_level)

    def test_refuel_increases_fuel_level(self):
        initial_fuel_level = self.car.fuel_level
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_level, initial_fuel_level + 20 if initial_fuel_level + 20 <= self.car.fuel_capacity else self.car.fuel_capacity)


if __name__ == '__main__':
    unittest.main()

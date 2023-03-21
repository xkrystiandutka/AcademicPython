from datetime import datetime


class Wheel:
    def __init__(self, color, material, state):
        self.color = color
        self.material = material
        self.state = state

    def change_state(self, new_state):
        self.state = new_state

    def print_info(self):
        print(f"This wheel is {self.color} and is made of {self.material} and is {self.state}.")


class Vehicle:
    def __init__(self, is_electric:bool, production_date:str, wheels):
        self.is_electric = is_electric
        self.production_date = production_date
        self.wheels = wheels

    def print_info(self):
        print("Vehicle information:")
        print(f"- Electric: {self.is_electric}")
        print(f"- Production date: {self.production_date}")
        print("Wheels:")
        for i, wheel in enumerate(self.wheels):
            print(f"- Wheel {i + 1}:")
            wheel.print_info()


class Car(Vehicle):
    def __init__(self, is_electric, production_date, wheels, license_category):
        super().__init__(is_electric, production_date, wheels)
        self.license_category = license_category

    def print_license_category(self):
        print(f"License category: {self.license_category}")


class Motorcycle(Vehicle):
    def __init__(self, is_electric, production_date, wheel1, wheel2, license_category):
        wheels = [wheel1, wheel2]
        super().__init__(is_electric, production_date, wheels)
        self.license_category = license_category

    def print_license_category(self):
        print(f"License category: {self.license_category}")


if __name__ == '__main__':
    # Create car object with 4 wheels
    car_wheels = [Wheel('red', 'steel', 'good'), Wheel('black', 'rubber', 'good'),
                  Wheel('silver', 'aluminum', 'good'), Wheel('blue', 'titanium', 'good')]
    car = Car(False, '2023-03-15', car_wheels, 'B')
    car.print_info()
    car.print_license_category()

    # Create motorcycle object with 2 wheels
    wheel1 = Wheel('red', 'steel', 'good')
    wheel2 = Wheel('red', 'steel', 'good')
    motorcycle = Motorcycle(False, '2023-03-15', wheel1, wheel2, 'A')
    motorcycle.print_info()
    motorcycle.print_license_category()

    # Change state of wheel
    wheel1.change_state('worn')
    motorcycle.print_info()
class Car:
    def __init__(self, speed=0, fuel_capacity=50, fuel_consumption=10):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        self.fuel_consumption = fuel_consumption


    def say_state(self):
        print("I'm going {} kph!".format(self.speed))


    def accelerate(self):
        self.speed += 5


    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5


    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


class Truck(Car):
    def __init__(self, speed=0, fuel_capacity=50, fuel_consumption=10, cargo_capacity=0, *args, **kwargs):
        super().__init__(speed, fuel_capacity, fuel_consumption, *args, **kwargs)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0

    def load_cargo(self, amount):
        if self.current_cargo + amount <= self.cargo_capacity:
            self.current_cargo += amount
            print("Loaded {} units of cargo.".format(amount))
        else:
            print("Cannot load {} units of cargo. Exceeds cargo capacity.".format(amount))

    def unload_cargo(self, amount):
        if self.current_cargo - amount >= 0:
            self.current_cargo -= amount
            print("Unloaded {} units of cargo.".format(amount))
        else:
            print("Cannot unload {} units of cargo. Insufficient cargo.".format(amount))


class PoliceCar(Car):
    def __init__(self, speed=0, fuel_capacity=50, fuel_consumption=10, siren=False, *args, **kwargs):
        super().__init__(speed, fuel_capacity, fuel_consumption, *args, **kwargs)
        self.siren = siren

    def turn_on_siren(self):
        self.siren = True
        print("Siren turned on.")

    def turn_off_siren(self):
        self.siren = False
        print("Siren turned off.")

    def is_siren_on(self):
        return self.siren

if __name__ == '__main__':
    my_truck = Truck(speed=30, fuel_capacity=100, fuel_consumption=15, cargo_capacity=500)
    my_truck.say_state()  # Output: I'm going 30 kph!

    my_truck.load_cargo(200)  # Output: Loaded 200 units of cargo.
    my_truck.load_cargo(400)  # Output: Cannot load 400 units of cargo. Exceeds cargo capacity.

    my_truck.accelerate()
    my_truck.say_state()  # Output: I'm going 35 kph!

    my_truck.unload_cargo(150)  # Output: Unloaded 150 units of cargo.
    my_truck.unload_cargo(100)  # Output: Unloaded 100 units of cargo.
    my_truck.unload_cargo(100)  # Output: Cannot unload 100 units of cargo. Insufficient cargo.

    my_police_car = PoliceCar(speed=60, fuel_capacity=80, fuel_consumption=8, siren=False)
    my_police_car.say_state()  # Output: I'm going 60 kph!

    my_police_car.turn_on_siren()  # Output: Siren turned on.
    print(my_police_car.is_siren_on())  # Output: True

    my_police_car.brake()
    my_police_car.say_state()  # Output: I'm going 55 kph!

    my_police_car.turn_off_siren()  # Output: Siren turned off.
    print(my_police_car.is_siren_on())  # Output: False

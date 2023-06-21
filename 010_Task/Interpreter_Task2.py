from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Boiler:
    def __init__(self):
        self.temperature = 83  # in celsius

    def __str__(self):
        return f'boiler temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the boiler's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the boiler's temperature by {amount} degrees")
        self.temperature -= amount


class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the air condition')
        self.is_on = True

    def turn_off(self):
        print('turning off the air condition')
        self.is_on = False


class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heating')
        self.is_on = False


class Fridge:
    def __init__(self):
        self.temperature = 2  # in celsius

    def __str__(self):
        return f'fridge temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f"increasing the fridge's temperature by {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self, amount):
        print(f"decreasing the fridge's temperature by {amount} degrees")
        self.temperature -= amount


def main():
    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    while True:
        print("Menu:")
        print("1. Open device")
        print("2. Close device")
        print("3. Increase temperature")
        print("4. Decrease temperature")
        print("Enter 'q' to quit.")

        user_input = input("Select an option (enter number): ")
        if user_input.lower() == 'q':
            break

        try:
            option = int(user_input)

            if option == 1:
                print("Available devices: gate, garage, air condition, heating")
                device_input = input("Enter the device name: ")
                if device_input == 'gate':
                    gate.open()
                elif device_input == 'garage':
                    garage.open()
                elif device_input == 'air condition':
                    airco.turn_on()
                elif device_input == 'heating':
                    heating.turn_on()
                else:
                    print("Invalid device.")

            elif option == 2:
                print("Available devices: gate, garage, air condition, heating")
                device_input = input("Enter the device name: ")
                if device_input == 'gate':
                    gate.close()
                elif device_input == 'garage':
                    garage.close()
                elif device_input == 'air condition':
                    airco.turn_off()
                elif device_input == 'heating':
                    heating.turn_off()
                else:
                    print("Invalid device.")

            elif option == 3:
                print("Available devices: boiler, fridge")
                device_input = input("Enter the device name: ")
                if device_input == 'boiler':
                    amount_input = input("Enter the amount to increase the temperature: ")
                    amount = int(amount_input)
                    boiler.increase_temperature(amount)
                elif device_input == 'fridge':
                    amount_input = input("Enter the amount to increase the temperature: ")
                    amount = int(amount_input)
                    fridge.increase_temperature(amount)
                else:
                    print("Invalid device.")

            elif option == 4:
                print("Available devices: boiler, fridge")
                device_input = input("Enter the device name: ")
                if device_input == 'boiler':
                    amount_input = input("Enter the amount to decrease the temperature: ")
                    amount = int(amount_input)
                    boiler.decrease_temperature(amount)
                elif device_input == 'fridge':
                    amount_input = input("Enter the amount to decrease the temperature: ")
                    amount = int(amount_input)
                    fridge.decrease_temperature(amount)
                else:
                    print("Invalid device.")

            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input.")
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == '__main__':
    main()

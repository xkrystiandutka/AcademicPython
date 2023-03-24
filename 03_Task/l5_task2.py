from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella ' 'bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3 # in seconds for the sake of the example


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f'preparing the {self.dough.name} '
        f'dough of your {self}...')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')

    def add_sauce(self, sauce):
        self.sauce = sauce
        print(f"Adding the {self.sauce.name.lower()} sauce to your {self}...")
        time.sleep(STEP_DELAY)
        print(f"Done with the {self.sauce.name.lower()} sauce.")

    def add_topping(self, *toppings):
        for topping in toppings:
            self.topping.append(topping)
            print(f"Adding {topping.name.lower()} to your {self}...")
            time.sleep(STEP_DELAY)
        print("Done with the toppings.")


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f'adding the tomato sauce to your {self.pizza}...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'
        if self.pizza.name == 'hawaiian':
            topping_desc = 'ham, pineapple, cheese'
        topping_items = (PizzaTopping.double_mozzarella,
        PizzaTopping.oregano)
        print(f'adding the topping ({topping_desc}) to your {self.pizza}')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your {self.pizza} for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f'your {self.pizza} is ready')


class HawaiianBuilder(MargaritaBuilder):
    def __init__(self):
        super().__init__()
        self.pizza.name = 'hawaiian'

    def add_ham(self):
        self.pizza.set_topping("ham")

    def add_pineapple(self):
        self.pizza.set_topping("pineapple")

    def add_cheese(self):
        self.pizza.set_topping("cheese")


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        self.pizza.add_sauce(PizzaSauce.creme_fraiche)
        self.pizza.sauce = PizzaSauce.creme_fraiche
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    def add_topping(self):
        topping_desc = 'mozzarella, bacon, ham, mushrooms, red onion, oregano'

        topping_items = (PizzaTopping.mozzarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregano)
        print(f'adding the topping ({topping_desc}) to your creamy bacon')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your creamy bacon for {self.baking_time} seconds')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder

        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        input_msg = 'What pizza would you like, [m]argarita or [c]reamy bacon or [h]awaiian?'
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only margarita (key m) or creamy bacon (key c) or hawaiian (key h) are available'
        print(error_msg)
        return False, None
    return True, builder


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder, h=HawaiianBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Enjoy your {pizza}!')


if __name__ == '__main__':
    main()

# Zaletą dziedziczenia jest to, że możemy dziedziczyć funkcjonalność z klasy bazowej i dostosowywać ją do naszych
# potrzeb, bez potrzeby ponownego kodowania całej klasy. Wadą jest to, że dziedziczenie może prowadzić do  zagnieżdżania klas,
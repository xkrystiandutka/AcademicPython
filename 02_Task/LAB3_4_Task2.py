import random

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Frog encounters {obstacle} and {act}!'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the Wizard battles against {obstacle} and {act}!'
        print(msg)

class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        if self.power >= obstacle.power:
            print(f'{self} defeats {obstacle}!')
        else:
            print(f'{self} is defeated by {obstacle}!')

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 5)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 10)

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 7)

class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class Obstacle:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return self.name

class FirePit(Obstacle):
    def __init__(self):
        super().__init__('a fiery pit', 7)

    def action(self):
        return 'burns you'

class ToxicSwamp(Obstacle):
    def __init__(self):
        super().__init__('a toxic swamp', 5)

    def action(self):
        return 'poisons you'

class EnemyCity(Obstacle):
    def __init__(self):
        super().__init__('an enemy city', 10)

    def action(self):
        return 'attacks you'

class GameEnvironment:
    def __init__(self, character, obstacle):
        self.hero = character
        self.obstacle = obstacle

    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    while True:
        try:
            age = int(input(f'Welcome {name}. How old are you? '))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_character():
    while True:
        try:
            choice = int(input('Choose your character:\n1. Warrior\n2. Mage\n3. Archer\n'))
            if choice == 1:
                name = input('Enter your warrior name: ')
                return Warrior(name)
            elif choice == 2:
                name = input('Enter your mage name: ')
                return Mage(name)
            elif choice == 3:
                name = input('Enter your archer name: ')
                return Archer(name)
            else:
                print('Invalid choice. Please try again.')
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_obstacle():
    obstacles = [FirePit(), ToxicSwamp(), EnemyCity()]
    return random.choice(obstacles)

def main():
    name = input("Hello. What's your name? ")
    age = validate_age(name)
    character = choose_character()
    obstacle = choose_obstacle()
    print(f'You are playing as {character}. Your first obstacle is {obstacle}.')
    game = GameEnvironment(character, obstacle)
    game.play()

if __name__ == '__main__':

    main()

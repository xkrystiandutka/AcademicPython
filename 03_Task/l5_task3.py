class Pizza:
    def __init__(self):
        self.garlic = False
        self.extra_cheese = False

    def with_garlic(self):
        self.garlic = True
        return self

    def with_extra_cheese(self):
        self.extra_cheese = True
        return self

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = (f'Garlic: {garlic}', f'Extra cheese: {cheese}')
        return '\n'.join(info)


class Pizza2:
    class PizzaBuilder2:
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza2(self)

    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = (f'Garlic: {garlic}', f'Extra cheese: {cheese}')
        return '\n'.join(info)


if __name__ == '__main__':
    pizza = Pizza().with_garlic().with_extra_cheese()
    print(pizza)  # Wersja wykorzystująca płynny wzór budowniczy jest bardziej elastyczna i intuicyjna w użyciu.
    pizza2 = Pizza2.PizzaBuilder2().add_garlic().add_extra_cheese().build()
    print(pizza2)  # Wersja zbudowana za pomocą klasy PizzaBuilder jest bardziej sztywna, ale bardziej modularna.


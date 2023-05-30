# Proszę dodać więcej obserwatorów. Na przykład, można dodać formater ósemkowy,
# formater liczb rzymskich lub dowolnego innego obserwatora, który używa twojej ulubionej
# reprezentacji.
class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' " \
               f"has data = {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify()


class HexFormatterObs:
    def notify(self, publisher):
        value = hex(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now hex data = {value}")


class BinaryFormatterObs:
    def notify(self, publisher):
        value = bin(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now bin data = {value}")


class OctalFormatterObs:
    def notify(self, publisher):
        value = oct(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now octal data = {value}")


# system rzymski
def to_roman(num):
    roman = ''
    for value, letter in [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                          (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                          (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]:
        while num >= value:
            roman += letter
            num -= value
    return roman

class RomanNumeralFormatterObs:
    def notify(self, publisher):
        value = to_roman(publisher.data)
        print(f"{type(self).__name__}: '{publisher.name}' has now roman numeral data = {value}")

class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return f"{type(self).__name__}: '{self.name}' " \
               f"has data = {self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f'Error: {e}')
        else:
            self.notify()


def main():
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatterObs()
    df.add(hf)
    df.data = 3
    print(df)
    print()
    bf = BinaryFormatterObs()
    df.add(bf)
    df.data = 21
    print(df)
    print()
    of = OctalFormatterObs()
    df.add(of)
    df.data = 42
    print(df)
    print()
    rf = RomanNumeralFormatterObs()
    df.add(rf)
    df.data = 1999
    print(df)
    print()
    df.remove(hf)
    df.data = 40
    print(df)
    print()
    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)
    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()

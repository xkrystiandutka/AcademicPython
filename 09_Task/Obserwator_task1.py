# Ten przykład byłby o wiele bardziej interesujący, gdyby był interaktywny. Nawet proste
# menu, które pozwala użytkownikowi na dołączanie/odłączanie obserwatorów w czasie
# wykonywania i modyfikowanie wartości DefaultFormatter byłoby dobre, ponieważ aspekt
# środowiska wykonawczego staje się bardziej widoczny. Proszę to zrobić.

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


def main():
    df = DefaultFormatter('test1')
    print(df)
    print()

    hf = HexFormatterObs()
    bf = BinaryFormatterObs()

    while True:
        print(f"Current value: {df.data}")
        print("1. Change value")
        print("2. Add HexFormatter observer")
        print("3. Add BinaryFormatter observer")
        print("4. Remove observer")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            new_value = input("Enter new value: ")
            df.data = new_value
        elif choice == '2':
            df.add(hf)
        elif choice == '3':
            df.add(bf)
        elif choice == '4':
            observer_choice = input("Enter observer to remove (h for hex, b for binary): ")
            if observer_choice == 'h':
                df.remove(hf)
            elif observer_choice == 'b':
                df.remove(bf)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

        print()

    print("Exiting program.")


if __name__ == '__main__':
    main()

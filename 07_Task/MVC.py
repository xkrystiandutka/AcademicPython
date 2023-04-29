quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...',
    'Facts are stubborn things.'
)


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value

#Należy dodać obsługę zakończenia działania programu po wybraniu odpowiedniej wartości,
#następnie dodać nowy widok, wyświetlający cytaty w nowy sposób oraz zmianę widoku po
#wybraniu odpowiedniej opcji.


class QuoteTerminalView:
    STANDARD_VIEW = "standard"
    FANCY_VIEW = "fancy"

    def __init__(self):
        self.current_view = self.STANDARD_VIEW

    def show(self, quote):
        if self.current_view == self.STANDARD_VIEW:
            print(f'And the quote is: "{quote}"')
        elif self.current_view == self.FANCY_VIEW:
            print('*' * 50)
            print(f'"{quote}"')
            print('*' * 50)

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input(f'Which quote number would you like to see? (current view: {self.current_view}) ')

    def select_view(self):
        valid_input = False
        while not valid_input:
            view = input("Select view (standard/fancy): ")
            if view.lower() == self.STANDARD_VIEW:
                self.current_view = self.STANDARD_VIEW
                valid_input = True
            elif view.lower() == self.FANCY_VIEW:
                self.current_view = self.FANCY_VIEW
                valid_input = True
            else:
                self.error(f"Incorrect view '{view}'")


class QuoteFancyView:
    def show(self, quote):
        print('*' * 50)
        print(f'"{quote}"')
        print('*' * 50)


class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                option = input("Select option (quote/view/quit): ")
                if option.lower() == "quote":
                    n = self.view.select_quote()
                    n = int(n)
                    quote = self.model.get_quote(n)
                    self.view.show(quote)
                elif option.lower() == "view":
                    self.view.select_view()
                elif option.lower() == "quit":
                    print("Quitting program...")
                    return
                else:
                    self.view.error(f"Incorrect option '{option}'")
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()

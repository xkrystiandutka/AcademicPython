import pickle


class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def save_state(self):
        current_state = pickle.dumps(self.__dict__)
        return current_state

    def restore_state(self, memento):
        previous_state = pickle.loads(memento)
        self.__dict__.clear()
        self.__dict__.update(previous_state)

    def __str__(self):
        return f'{self.text} - By {self.author}.'


def main():
    quotes = []

    while True:
        print('--- Quote Management System ---')
        print('1. Add a new quote')
        print('2. View all quotes')
        print('3. Restore a previous state')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            text = input('Enter the quote text: ')
            author = input('Enter the author: ')
            quote = Quote(text, author)
            quotes.append(quote)
            print('Quote added successfully!')

        elif choice == '2':
            if not quotes:
                print('No quotes available.')
            else:
                print('--- All Quotes ---')
                for i, quote in enumerate(quotes):
                    print(f'{i + 1}. {quote}')

        elif choice == '3':
            if not quotes:
                print('No quotes available.')
            else:
                print('--- Restore State ---')
                print('Select a quote to restore:')
                for i, quote in enumerate(quotes):
                    print(f'{i + 1}. {quote}')
                selection = input('Enter the number of the quote: ')
                try:
                    quote_index = int(selection) - 1
                    if quote_index >= 0 and quote_index < len(quotes):
                        quote = quotes[quote_index]
                        memento = quote.save_state()
                        quote.restore_state(memento)
                        print('Quote state restored successfully!')
                    else:
                        print('Invalid selection.')
                except ValueError:
                    print('Invalid selection.')

        elif choice == '4':
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()

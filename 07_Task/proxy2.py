import secrets
# Podstawową zasadą bezpieczeństwa jest to, że nigdy nie powinniśmy przechowywać
# haseł jednoznacznych. Bezpieczne przechowywanie hasła nie jest zbyt trudne, o ile wiemy,
# których bibliotek należy użyć przechowywania tajnej wiadomości na zewnątrz (na przykład w pliku lub bazie danych).
from abc import ABC, abstractmethod


#  zapis tajnej wiadomości.
def save_secret(secret):
    with open('secret.txt', 'w') as f:
        f.write(secret)

# odczyt tajnej wiadomości.
def load_secret():
    with open('secret.txt', 'r') as f:
        secret = f.read()
    return secret


# W celu zabezpieczenia aplikacji przed bezpośrednim tworzeniem instancji klasy SensitiveInfo, wymuszam dziedziczenie klasy SensitiveInfo z SensitiveInfoBase.
# utworzone metody read i add. Klasa SensitiveInfo  dziedziczyć po SensitiveInfoBase.

class SensitiveInfoBase(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, user):
        pass

    @abstractmethod
    def remove(self, user):
        pass


class SensitiveInfo(SensitiveInfoBase):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
        self.secret = secrets.token_hex(16)

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')

#Aplikacja obsługuje tylko dodawanie nowych użytkowników, ale co z usunięciem istniejącego
# użytkownika? Należy dodać metodę remove()

    def remove(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f'Removed user {user}')
        else:
            print(f'User {user} not found')


class Info:
    """protection proxy to SensitiveInfo"""

    def __init__(self):
        self.protected = SensitiveInfo()
        # self.secret = '0xdeadbeef'
        self.secret = load_secret()

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")

    def remove(self, user):
        sec = input('what is the secret? ')
        self.protected.remove(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. remove user |==| 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('choose username: ')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    secret = secrets.token_hex(16)
    save_secret(secret)
    main()

# Przykład implementacji Pełnomocnika ochraniającego ma bardzo dużą lukę
# w zabezpieczeniach. Nic nie stoi na przeszkodzie, aby kod klienta pomijał bezpieczeństwo
# aplikacji, tworząc bezpośrednio instancję SensitiveInfo. Należy ulepszyć przykład, aby
# zapobiec tej sytuacji. Jednym ze sposobów jest użycie modułu abc do zakazania
# bezpośredniego tworzenia instancji SensitiveInfo. Jakie inne zmiany kodu są wymagane
# w tym przypadku?
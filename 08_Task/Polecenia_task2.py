# Zobaczmy, co można poprawić w naszym przykładzie implementacji poleceń. Wśród
# rzeczy do rozważenia są:
# • Co się stanie, jeśli spróbujemy zmienić nazwę pliku, który nie istnieje?
# • Co z plikami, które istnieją, ale nie można zmienić ich nazwy, ponieważ nie mamy
# odpowiednich uprawnień do systemu plików

# W przypadku próby zmiany nazwy pliku, który nie istnieje, zostanie zgłoszony wyjątek FileNotFoundError.
# Możemy dodać obsługę tego wyjątku do metody execute() klasy RenameFile, aby wyświetlić stosowny komunikat.
# W przypadku braku uprawnień do systemu plików, wywołanie os.rename() zwróci wyjątek PermissionError.
# Możemy również dodać obsługę tego wyjątku do metody execute() klasy RenameFile i wyświetlić stosowny komunikat.
import os

verbose = True


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        try:
            os.rename(self.src, self.dest)
        except FileNotFoundError:
            print(f"File '{self.src}' not found")
        except PermissionError:
            print(f"Permission denied to rename file '{self.src}'")

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        try:
            os.rename(self.dest, self.src)
        except FileNotFoundError:
            print(f"File '{self.dest}' not found")
        except PermissionError:
            print(f"Permission denied to rename file '{self.dest}'")

    def supported_undo(self):
        return True



def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile(orig_name, new_name))
    [c.execute() for c in commands]
    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()
    for c in reversed(commands):
        try:
            if c.supported_undo():
                c.undo()
        except AttributeError as e:
            print("Error", str(e))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")
        exit()
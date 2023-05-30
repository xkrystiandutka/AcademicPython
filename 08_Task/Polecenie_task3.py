import os

verbose = True


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
        try:
            delete_file(self.path)
        except:
            print('delete action not successful...')
            print('... file was probably already deleted.')


def delete_file(path):
    if verbose:
        print(f"deleting file {path}...")
    os.remove(path)


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        try:
            os.rename(self.src, self.dest)
        except:
            print('rename action not successful...')
            print('... file was probably not found.')

    def undo(self):
        try:
            os.rename(self.dest, self.src)
        except:
            print('undo rename action not successful...')
            print('... file may have been deleted or renamed again.')


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = [CreateFile(orig_name)]
    commands.append(RenameFile(orig_name, new_name))
    for c in commands:
        try:
            c.execute()
        except AttributeError as e:
            print(f"Error: {str(e)}")

    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()

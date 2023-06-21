import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]

LIMIT = 5  # in characters


def all_unique_sort(s):
    srt_str = sorted(s)
    for (c1, c2) in pairs(srt_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s):
    return True if len(set(s)) == len(s) else False


def all_unique(word):
    if len(word) > LIMIT:
        return all_unique_sort(word)
    else:
        return all_unique_set(word)


def main():
    WORD_IN_DESC = 'Insert word (type quit to exit)> '

    while True:
        word = None
        while not word:
            word = input(WORD_IN_DESC)
            if word == 'quit':
                print('bye')
                return

        result = all_unique(word)
        print(f'allUnique({word}): {result}')


if __name__ == '__main__':
    main()

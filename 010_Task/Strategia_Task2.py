class AllUnique:
    LIMIT = 5  # in characters
    SLOW = 3  # in seconds
    WARNING = 'the algorithm is a little bit slow'

    @staticmethod
    def pairs(seq):
        n = len(seq)
        for i in range(n):
            yield seq[i], seq[(i + 1) % n]

    @staticmethod
    def all_unique_sort(s):
        if len(s) > AllUnique.LIMIT:
            print(AllUnique.WARNING)
            # time.sleep(AllUnique.SLOW)

        srt_str = sorted(s)
        for (c1, c2) in AllUnique.pairs(srt_str):
            if c1 == c2:
                return False
        return True

    @staticmethod
    def all_unique_set(s):
        if len(s) < AllUnique.LIMIT:
            print(AllUnique.WARNING)
            # time.sleep(AllUnique.SLOW)

        return True if len(set(s)) == len(s) else False

    @staticmethod
    def test(word):
        result = AllUnique.all_unique_set(word)
        print(f'allUnique({word}): {result}')


if __name__ == '__main__':
    word = input('Insert word (type quit to exit)> ')
    if word != 'quit':
        AllUnique.test(word)

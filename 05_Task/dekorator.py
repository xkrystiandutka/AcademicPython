sum_cache = {0: 0}


def number_sum(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n - 1)
    # Add the value to the cache
    sum_cache[n] = res
    return res


cache_fib = {0: 0, 1: 1}


def fibonacci(n):
    """Returns the suite of Fibonacci numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n in cache_fib:
        return cache_fib[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    cache_fib[n]


if __name__ == '__main__':
    from timeit import Timer

    t = Timer('number_sum(300)', 'from __main__ import number_sum')
    print('Time: ', t.timeit())

#kodu opartego na memoizacji poprawa wydajnosci  wykonania Time: z 3.46 dla sumy 30 liczb na 0.11 dla sumy 300
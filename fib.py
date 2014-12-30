__author__ = 'kristofleroux'

def fib(n):
    a, b = 0, 1

    for i in xrange(n-2):
        a, b = b, a + b

    return b

if __name__ == "__main__":
    print fib(10)

    import itertools

    print list(itertools.cycle([1,2,-1, -2], 2))
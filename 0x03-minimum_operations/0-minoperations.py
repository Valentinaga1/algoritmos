
#!/usr/bin/python3
""" method that calculates the fewest number of operations needed to result
in exactly n H characters in the file. """


def minOperations(n):
    """ Function """
    if not isinstance(n, int) or n < 2:
        return 0
    op = 0
    k = 3
    while n % 2 == 0:
        op += 2
        n = n//2
    while k <= n:
        while n % k == 0:
            op += k
            n = n//k
        k += 2
    return int(op)

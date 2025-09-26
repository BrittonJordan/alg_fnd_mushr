
def compute_fibonacci(n):
    """Return the nth Fibonacci number.

    >>> compute_fibonacci(0)
    0
    >>> compute_fibonacci(1)
    1
    >>> compute_fibonacci(2)  # 0 + 1
    1
    >>> compute_fibonacci(3)  # 1 + 1
    2
    >>> compute_fibonacci(4)  # 1 + 2
    3
    """
    # BEGIN QUESTION 1.1
    "*** REPLACE THIS LINE ***"

    if n == 0:
        return 0

    curr = 1
    past = 0
    for _ in range(n - 1):
        new_past = curr
        curr = past + curr
        past = new_past
    
    return curr


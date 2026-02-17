"""Task 3: Control Structures."""


def check_sign(number: float) -> str:
    """Return whether a number is 'positive', 'negative', or 'zero'."""
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def first_n_primes(n: int) -> list[int]:
    """Return a list of the first n prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = all(candidate % p != 0 for p in primes if p * p <= candidate)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes


def sum_one_to_n(n: int) -> int:
    """Return the sum of all integers from 1 to n (inclusive) using a while loop."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


if __name__ == "__main__":
    # if/elif/else demo
    for num in (-5, 0, 7):
        print(f"{num} is {check_sign(num)}")

    # for loop: first 10 primes
    primes = first_n_primes(10)
    print(f"First 10 primes: {primes}")

    # while loop: sum 1-100
    total = sum_one_to_n(100)
    print(f"Sum of 1 to 100: {total}")

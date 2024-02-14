def getPrimeNumbers(n):
    """
    Returns a list of prime numbers between 2 and n (inclusive).

    Args:
        n: The upper limit for the prime number search (inclusive).

    Returns:
        A list of prime numbers between 2 and n.

    Raises:
        ValueError: If n is less than 2.
    """

    if n < 2:
        raise ValueError("n must be greater than or equal to 2")

    primes = [2]  # Initialize with 2 as the first prime number

    # Check for odd numbers only, as even numbers cannot be prime (except 2)
    for num in range(3, n + 1, 2):
        isPrime = True
        # Check divisibility only up to the square root of the number
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)

    return primes

# Example usage
primes = getPrimeNumbers(10)
print(primes)  # Output: [2, 3, 5, 7]

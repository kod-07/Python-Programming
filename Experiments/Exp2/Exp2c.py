def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(lower, upper):
    """Generate prime numbers in the given interval [lower, upper]."""
    prime_numbers = []
    for num in range(lower, upper + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Get user input for the interval
lower_bound = int(input("Enter the lower bound of the interval: "))
upper_bound = int(input("Enter the upper bound of the interval: "))

# Generate and print prime numbers in the interval
primes = generate_primes(lower_bound, upper_bound)
print(f"Prime numbers between {lower_bound} and {upper_bound} are: {primes}")

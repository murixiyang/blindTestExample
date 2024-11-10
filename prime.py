def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input from the user
n = int(input("Enter a number: "))
print("Prime numbers from 1 to", n, "are:", print_primes(n))

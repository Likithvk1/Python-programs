def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(M, N):
    primes = [num for num in M + N if is_prime(num)]
    return len(primes), primes

# Example usage
M = [3, 8, 11, 15, 19]
N = [2, 9, 13, 22, 29]

total_primes, primes_list = find_primes(M, N)

print(f"Total number of primes: {total_primes}")
print(f"Primes in both arrays: {primes_list}")

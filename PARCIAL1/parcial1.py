class PrimeNumbers:
    def __init__(self):
        self.__primes = []

    def __is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(self, limit):
        self.__primes = [num for num in range(2, limit + 1) if self.__is_prime(num)]

    def get_primes(self):
        return self.__primes

if __name__ == "__main__":
    limit = int(input("Introduce un número entero: "))
    primes_generator = PrimeNumbers()
    primes_generator.generate_primes(limit)
    print(f"Números primos menores o iguales a {limit}: {primes_generator.get_primes()}")

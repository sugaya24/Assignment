# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

""" Primes, GCD, LCM """
import math


def is_prime(n):
    """ Check if n is prime """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(is_prime(4))


def gcd(a, b):
    """ GCD of a and b """
    # using recursion
    # if b == 0:
    #     return a
    # else:
    #     return gcd(b, a % b)

    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        while b != 0:
            a, b = b, a % b
        return a


print(gcd(270, 192))  # 6
print(gcd(192, 270))  # 6
print(gcd(192, 0))  # 192


def lcm(a, b):
    """ LCM of a and b """
    # gcd * lcm = a * b
    # lcm = a * b // gcd
    return a * b // gcd(a, b)


print(lcm(18, 30))  # 90


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    list = []
    for i in range(n):
        if is_prime(i) and i > 1:
            list.append(i)
    return list


print(generate_primes(100))

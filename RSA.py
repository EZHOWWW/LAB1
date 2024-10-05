
def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n <= 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def generate_keypair(p: int , q: int) -> tuple:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    phi = (p-1) * (q-1)
    
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def gcd(n1: int, n2: int) ->int:
    return math.gcd(n1,n2)

def Euclid(a, b):
    res = [(a,b)]
    while a % b != 0:
        c = a % b
        a = b
        b = c
        res.append((a,b))
    return res


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """
    x0,x1 = 0, 0
    y0, y1 = 1, 1
    for i in Euclid(phi, e)[-2::-1]:
        x0 = y1
        y0 = x1 - y1 * (i[0] // i[1])
        y1 = y0
        x1 = x0
    return y0 % phi
print(multiplicative_inverse(7, 40))
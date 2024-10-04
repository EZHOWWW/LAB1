def get_displace_char(char: str, key: int = 3) -> str:
    """ord(A) = 65, ord(Z) = 90
    ord(a) = 97, ord(z)= 122"""
    _ord = ord(char[0])
    if 65 <= _ord <= 90:
        return chr(65 + (_ord + key - 65) % 26)
    elif 97 <= _ord <= 122:
        return chr(97 + (_ord + key - 97) % 26)
    return char


def encrypt_caesar(plaintext: str, key: int = 3) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    return "".join(get_displace_char(c, key) for c in plaintext)


def decrypt_caesar(ciphertext: str, key: int = 3) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    return "".join(get_displace_char(c, -key) for c in plaintext)

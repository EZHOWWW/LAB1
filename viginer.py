def get_displace_char(char: str, key: int) -> str:
    """ord(A) = 65, ord(Z) = 90
    ord(a) = 97, ord(z)= 122"""
    _ord = ord(char[0])
    if 65 <= _ord <= 90:
        return chr(65 + (_ord + key - 65) % 26)
    elif 97 <= _ord <= 122:
        return chr(97 + (_ord + key - 97) % 26)
    return char


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.lower()
    for i in range(len(plaintext)):
        ciphertext += get_displace_char(
            plaintext[i], -97 + ord(keyword[i % len(keyword)])
        )
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.lower()
    for i in range(len(ciphertext)):
        plaintext += get_displace_char(
            ciphertext[i], 97 - ord(keyword[i % len(keyword)])
        )
    return plaintext
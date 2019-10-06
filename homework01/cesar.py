def encrypt_caesar(plaintext: str) -> str:
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
    ciphertext = ""
    global ciphertext
    for char in plaintext:
        if char.isalpha():
            if ('X' <= char <= 'Z') or ('x' <= char <= 'z'):
                c = chr(ord(char) - (ord('Z') + 1 - ord('A')))
            char = chr(ord(char) + 3)
        ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
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
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if ('A' <= char <= 'C') or ('a' <= char <= 'c'):
                c = chr(ord(char) - (ord('A') + 1 - ord('Z')))
            char = chr(ord(char) + 3)
        ciphertext += char
    return plaintext

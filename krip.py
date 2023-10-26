def encrypt(plain_text, a, b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(
                    (a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                encrypted_char = chr(
                    (a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, a, b):
    decrypted_text = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(
                    (a_inverse * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                decrypted_char = chr(
                    (a_inverse * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


# Contoh penggunaan
plain_text = "FEITICEIRA"
a = 5
b = 10
encrypted_text = encrypt(plain_text, a, b)
decrypted_text = decrypt(encrypted_text, a, b)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

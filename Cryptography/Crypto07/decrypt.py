import Crypto.Cipher
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

iv = b'\x00' * 8
text = 'La lunghezza di questa frase non è divisibile per 8'
key = bytes.fromhex('7020ba37b26491b3')
cipher = DES.new(key, DES.MODE_CBC, iv=iv)

ciphertext = cipher.encrypt(
    pad(
        text.encode(),
        8,
        style='x923'
    )
)
print(f'Key: {key.hex()}')

# Nuovo oggetto decifratura
decipher = DES.new(key, DES.MODE_CBC, iv=iv)

# Rimozione padding x923 dopo decrittazione
plaintext = unpad(decipher.decrypt(ciphertext), 8, style='x923')
print(f'Plaintext: {plaintext.decode()}')

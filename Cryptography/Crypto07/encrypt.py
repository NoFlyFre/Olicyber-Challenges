import Crypto.Cipher
from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad

'''
Cipher = DES
Mode of operation = CBC
key.hex() = '57548e9218b3955d' <---- diversa ogni volta!!!
plaintext = 'La lunghezza di questa frase non è divisibile per 8'
Padding scheme = x923
'''
iv = b'\x00' * 8
text = 'La lunghezza di questa frase non è divisibile per 8'
key = bytes.fromhex('69cc857776ca8059')
cipher = DES.new(key, DES.MODE_CBC, iv=iv)

ciphertext = cipher.encrypt(
    pad(
        text.encode(),
        8,
        style='x923'
    )
)
print("==================")
print(f'Plaintext: \n{text}')
print(f'Key: \n{key.hex()}')
print(f'IV: \n{iv.hex()}')
print(f'Ciphertext: \n{ciphertext.hex()}')
print("==================")

"_________________________________ PARTE 2 ______________________________" 

'''
Cipher = AES256
Mode of operation = CFB
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
Padding scheme = pkcs7 (block size = 16)
Segment size = 24
'''

iv = b'\x00' * 16
text = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
key = bytes.fromhex('57548e9218b3955d57548e9218b3955d57548e9218b3955d57548e9218b3955d')
cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=24)

ciphertext = cipher.encrypt(
    pad(
        text.encode(),
        16,
        style='pkcs7'
    )
)
print("==================")
print(f'Plaintext: \n{text}')
print(f'Key: \n{key.hex()}')
print(f'IV: \n{iv.hex()}')
print(f'Ciphertext: \n{ciphertext.hex()}')
print("==================")

"_________________________________ PARTE 3 ______________________________" 

'''
Cipher = ChaCha20
key.hex() = '32a1711a4ddcbc0825114ed57c1bef10dd9ea6dfe97794cfaee68694ffd06132'
ciphertext.hex() = 'd99a9114a7191f63c89a1ef703f27d68e90b0bc67a149dac097c7fc8'
Nonce = cipher.nonce.hex() = '07d59e9274084a22'
'''

nonce = bytes.fromhex('07d59e9274084a22')
key = bytes.fromhex('32a1711a4ddcbc0825114ed57c1bef10dd9ea6dfe97794cfaee68694ffd06132')
cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = bytes.fromhex('d99a9114a7191f63c89a1ef703f27d68e90b0bc67a149dac097c7fc8')

text = cipher.decrypt(ciphertext)

print("==================")
print(f'Key: \n{key.hex()}')
print(f'None: \n{nonce.hex()}')
print(f'Ciphertext: \n{ciphertext.hex()}')
print(f'Plaintext: \n{text.decode()}')
print("==================")

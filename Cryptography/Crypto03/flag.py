from base64 import b64decode

cipher_b64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
cipher_dec = 664813035583918006462745898431981286737635929725

plain_b64 = b64decode(cipher_b64).decode("utf-8")
plain_dec = cipher_dec.to_bytes(cipher_dec.bit_length(), 'big').decode("utf-8")

plain = plain_b64 + plain_dec
print(plain)
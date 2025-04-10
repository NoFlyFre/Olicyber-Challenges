cipher = "104e137f425954137f74107f525511457f5468134d7f146c4c"
cipher_bytes = bytes.fromhex(cipher)

for key in range(256):
    plaintext = ''
    for b in cipher_bytes:
        p = b ^ key
        if 32 <= p <= 126:  
            plaintext += chr(p)
        else:
            break  
    else:
        print(f"Chiave: {key} (0x{key:02x}) => {plaintext}")
        print(f"Flag: flag{{{plaintext}}}")

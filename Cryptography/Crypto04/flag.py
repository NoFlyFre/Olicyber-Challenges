def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

m1_bytes = bytes.fromhex(m1)
m2_bytes = bytes.fromhex(m2)

flag = xor(m1_bytes, m2_bytes)
print(flag.decode("utf-8"))
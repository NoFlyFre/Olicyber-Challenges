cipher = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"

bytes = bytes.fromhex(cipher)

plain = bytes.decode("utf-8")

print(plain)
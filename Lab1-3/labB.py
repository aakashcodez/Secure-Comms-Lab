ciphertext = "66475 19274 92028 78494 24146 68542 17507 39398 32348 59378 70636"
key = "66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074"

ciphertext = ciphertext.replace(" ", "")
key = key.replace(" ", "")

result = ""

for c, k in zip(ciphertext, key):
    result += str((int(c) + int(k)) % 10)

checkerboard = {
    "0": "A", "1": "T", "3": "O", "4": "N",
    "5": "E", "7": "S", "8": "I", "9": "R",
    "20": "B", "21": "C", "22": "D", "23": "F",
    "24": "G", "25": "H", "26": "J", "27": "K",
    "28": "L", "29": "M",
    "60": "P", "61": "Q", "62": "U", "63": "V",
    "64": "W", "65": "X", "66": "Y", "67": "Z"
}

plaintext = ""
i = 0

while i < len(result):
    if result[i] in ("2", "6"):
        plaintext += checkerboard[result[i:i+2]]
        i += 2
    else:
        plaintext += checkerboard[result[i]]
        i += 1

print("Ciphertext:", " ".join(
    ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)
))

print("Key:", " ".join(
    key[i:i+5] for i in range(0, len(key), 5)
))

print("Result:", " ".join(
    result[i:i+5] for i in range(0, len(result), 5)
))

print("Plaintext:", plaintext)

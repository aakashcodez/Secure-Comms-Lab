import hashlib

salt = b"www.exploringsecurity.com"

hashes = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

remaining = {h: user for user, h in hashes.items()}

def generate_variations(word):
    forms = {
        word,
        word.lower(),
        word.upper(),
        word.capitalize()
    }

    for form in forms:
        if 5 <= len(form) <= 7:
            yield form

        for number in range(100):
            candidate = form + f"{number:02d}"
            if 5 <= len(candidate) <= 7:
                yield candidate

with open("/usr/share/wordlists/rockyou.txt",
          "r", encoding="latin-1") as file:

    for word in file:
        word = word.strip()

        for password in generate_variations(word):

            result = hashlib.sha1(
                salt + password.encode()
            ).hexdigest()

            if result in remaining:
                username = remaining.pop(result)
                print(f"[CRACKED] {username}: {password}")

        if not remaining:
            break

print("\nUncracked accounts:")
for username in remaining.values():
    print(username)

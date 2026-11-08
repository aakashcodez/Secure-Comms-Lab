import hashlib

SALT = "www.exploringsecurity.com"

TARGETS = {
    "Sparky": "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "Mark123": "92e54f10103a3c511853c7098c04141f114719c1",
    "superman": "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9",
    "security": "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "Tomtom": "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2",
    "JillC": "f44f3b09df53c1c11273def13cacd8922a86d48c"
}

remaining = {h: user for user, h in TARGETS.items()}

with open("/usr/share/wordlists/rockyou.txt", "rb") as file:
    for line in file:
        password = line.rstrip(b"\r\n")

        hashed = hashlib.sha1(
            SALT.encode() + password
        ).hexdigest()

        if hashed in remaining:
            username = remaining.pop(hashed)

            print(
                f"[CRACKED] {username}: "
                f"{password.decode('utf-8', errors='replace')}"
            )

        if not remaining:
            break

print("\nUncracked accounts:")
for username in remaining.values():
    print(username)

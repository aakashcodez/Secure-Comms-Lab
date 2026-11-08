#!/usr/bin/env python3
"""
Lab 08 - Salted Hashes
Verification: recompute SHA1(salt + password) for every recovered password
and confirm it reproduces the hash from the database dump.
"""
import hashlib

SALT = "www.exploringsecurity.com"

DUMP = {
    "Sparky":   ("Admin", "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef"),
    "Mark123":  ("user",  "92e54f10103a3c511853c7098c04141f114719c1"),
    "superman": ("user",  "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9"),
    "security": ("user",  "fafa4483874ec051989d53e1e432ba3a6c6b9143"),
    "Tomtom":   ("user",  "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2"),
    "JillC":    ("user",  "f44f3b09df53c1c11273def13cacd8922a86d48c"),
}

# Passwords recovered so far (JillC filled in if/when brute force returns)
RECOVERED = {
    "Tomtom":   "54321",
    "security": "121298",
    "superman": "qwerty",
    "Mark123":  "Mark123",
    "Sparky":   "Admin09",
    "JillC":    "Q2w13sA",
}

def sha1_salted(pw):
    return hashlib.sha1((SALT + pw).encode()).hexdigest()

print(f"Salt = {SALT!r}   scheme = SHA1(salt + password)\n")
print(f"{'User':10}{'Role':7}{'Password':12}{'Match':7}Hash")
print("-" * 78)
for user, (role, h) in DUMP.items():
    pw = RECOVERED.get(user)
    if pw is None:
        print(f"{user:10}{role:7}{'(uncracked)':12}{'--':7}{h}")
        continue
    ok = sha1_salted(pw) == h
    print(f"{user:10}{role:7}{pw:12}{'OK' if ok else 'FAIL':7}{h}")
print("-" * 78)
print(f"Recovered {len(RECOVERED)}/{len(DUMP)} passwords; "
      f"all recovered hashes verified = "
      f"{all(sha1_salted(p)==DUMP[u][1] for u,p in RECOVERED.items())}")

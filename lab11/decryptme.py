
#!/usr/bin/env python3

import argparse
import base64
import codecs
import string
from pathlib import Path

# Reverse the Caesar +4 transformation
LOWER = string.ascii_lowercase
REVERSE_CAESAR = str.maketrans(
    LOWER, LOWER[-4:] + LOWER[:-4]
)

# Forward Caesar +4, used for verification
FORWARD_CAESAR = str.maketrans(
    LOWER, LOWER[4:] + LOWER[:4]
)


def decode_layer(data):
    """Reverse one numbered encoding layer."""
    marker = data[0]
    payload = data[1:]

    if marker == "1":
        return codecs.decode(payload, "rot_13")

    if marker == "2":
        decoded = base64.b64decode(
            payload, validate=True
        )
        return decoded.decode("utf-8")

    if marker == "3":
        return payload.translate(REVERSE_CAESAR)

    raise ValueError(f"Unknown marker: {marker}")


def encode_layer(data, marker):
    """Reapply one encoding layer."""
    if marker == "1":
        result = codecs.encode(data, "rot_13")

    elif marker == "2":
        result = base64.b64encode(
            data.encode("utf-8")
        ).decode("ascii")

    elif marker == "3":
        result = data.translate(FORWARD_CAESAR)

    else:
        raise ValueError("Invalid encoding marker")

    return marker + result


def decrypt(ciphertext, verbose=False):
    data = ciphertext.strip()
    original = data
    markers = []

    for round_number in range(1, 10001):
        if not data or data[0] not in "123":
            break

        marker = data[0]
        data = decode_layer(data)
        markers.append(marker)

        if verbose:
            print(
                f"Layer {round_number:02d}: "
                f"Step {marker} | "
                f"Length: {len(data)}"
            )
    else:
        raise RuntimeError("Layer limit exceeded")

    # Re-encode using the reversed marker order
    rebuilt = data

    for marker in reversed(markers):
        rebuilt = encode_layer(rebuilt, marker)

    verified = rebuilt == original

    print("\n========== RESULTS ==========")
    print("Decoded plaintext:", data)
    print("Layers reversed:", len(markers))
    print("Original count:", len(markers) - 1)

    print("\nTransformation counts:")
    for marker in "123":
        print(f"Step {marker}: {markers.count(marker)}")

    print("\nDecoding marker sequence:")
    print("".join(markers))

    print("\nVerification:")
    print(
        "PASS - ciphertext reproduced exactly"
        if verified else
        "FAIL - ciphertext mismatch"
    )

    return data


def main():
    parser = argparse.ArgumentParser(
        description="Lab 11 intercepted message decoder"
    )
    parser.add_argument("file", help="Ciphertext file")
    parser.add_argument(
        "--trace", "-v",
        action="store_true",
        help="Show individual decoding layers"
    )
    args = parser.parse_args()

    ciphertext = Path(args.file).read_text(
        encoding="utf-8"
    ).strip()

    decrypt(ciphertext, args.trace)


if __name__ == "__main__":
    main()

# Lab 11 – Intercepted Message Decryption

This lab involves recovering an intercepted message using a partially damaged Python encryption script.

The original program applies multiple layers of ROT13, Base64 and Caesar shift operations. A Python 3 decoder was developed to reverse these transformations and recover the original message.

## Files

- `decryptme.py` – Python script used to decode and verify the intercepted message.

## Running the decoder

Place `intercepted.txt` in the same directory as the Python script and run:

```bash
python3 decryptme.py intercepted.txt --trace
```

The `--trace` option displays each decoding layer.

## Results

- Total encoding layers reversed: 68
- ROT13 operations: 22
- Base64 operations: 23
- Caesar shift operations: 23
- Original encoding count: 67
- Re-encoding verification: PASS

**Recovered message:** Why do elephants have big ears?

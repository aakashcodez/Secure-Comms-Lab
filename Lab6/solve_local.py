import sys
from collections import Counter
from PIL import Image

# Usage: python3 solve_local.py /path/to/aes.bmp.enc
# Defaults to aes.bmp.enc in the same folder you run it from.
path = sys.argv[1] if len(sys.argv) > 1 else "aes.bmp.enc"
W, H = 640, 480  # 54 + 640*480*3 = 921654 = file size

data = open(path, "rb").read()
print(f"Read {len(data)} bytes from {path}")

# 1) Rebuild the picture: drop the encrypted 54-byte header, treat the rest as
#    raw pixels, and flip because BMP rows are stored bottom-up.
body = data[54:]
img = Image.frombytes("RGB", (W, H), body[: W * H * 3]).transpose(Image.FLIP_TOP_BOTTOM)
img.save("recovered_flipped.png")

# 2) Clean mask: the most common 16-byte block is the background.
blocks = [data[i:i + 16] for i in range(0, len(data) - 15, 16)]
bg = Counter(blocks).most_common(1)[0][0]
wb = W * 3 // 16  # 120 blocks per row
mask = Image.new("L", (wb, H))
px = mask.load()
for i, b in enumerate(blocks[: wb * H]):
    px[i % wb, i // wb] = 255 if b == bg else 0
mask.transpose(Image.FLIP_TOP_BOTTOM).resize((960, 720), Image.NEAREST).save("mask.png")

print("Wrote recovered_flipped.png and mask.png")

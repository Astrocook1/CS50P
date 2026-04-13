import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1].strip()
after = sys.argv[2].strip()

valid_extensions = [".jpg", ".jpeg", ".png"]

format_before = before.lower()[-4:] if before.lower().endswith(".jpg") or before.lower().endswith(".png") else before.lower()[-5:]
format_after = after.lower()[-4:] if after.lower().endswith(".jpg") or after.lower().endswith(".png") else after.lower()[-5:]

if format_before not in valid_extensions:
    sys.exit("Invalid input")
elif format_after not in valid_extensions:
    sys.exit("Invalid output")
elif format_before != format_after:
    sys.exit("Input and output have different extensions")

shirt = "shirt.png"

try:
    with Image.open(before) as before:
        with Image.open(shirt) as shirt:
            size = shirt.size
            before = ImageOps.fit(before, size)
            before.paste(shirt, shirt)
            before.save(after)
except FileNotFoundError:
    sys.exit("Input does not exist")

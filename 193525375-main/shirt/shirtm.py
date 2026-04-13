import sys
from PIL import Image, ImageOps

if (len(sys.argv) - 1) < 2:
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) - 1) > 2:
    sys.exit("Too many command-line arguments")

before = sys.argv[1].strip()
after = sys.argv[2].strip()
shirt = "shirt.png"

format_before = before[len(before)-4:].lower()
format_after = after[len(after)-4:].lower()
before = before[:-4] + (format_before)
after = after[:-4] + (format_after)
print(format_before)

if not(format_before == ".png" or ".jpg" or ".jpeg"):
    sys.exit("Invalid input")
elif not(format_after == ".png" or ".jpg" or ".jpeg"):
    sys.exit("Invalid output")
elif format_before != format_after:
    sys.exit("Input and output have different extensions")

try:
    with Image.open(shirt) as shirt:
        with Image.open(before) as before:
            before = before.convert("RGBA")
            shirt = shirt.convert("RGBA")
            size = shirt.size
            before = ImageOps.fit(before, size, method = Image.Resampling.LANCZOS)
            before.paste(shirt,shirt)
            before = before.convert("RGB")
            before.save(after)
    #before.paste(before, shirt).save(after)

except(FileNotFoundError):
    sys.exit("Input does not exist")

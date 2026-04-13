from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    figlet.setFont(font = choice(fonts))
elif len(sys.argv) == 3 and sys.argv[2] in fonts:
    if sys.argv[1].startswith("-f") or sys.argv[1].startswith("--font"):
        figlet.setFont(font = sys.argv[2])
    else:
       sys.exit("Invalid usage")
elif sys.argv[2] not in fonts:
    sys.exit("Invalid usage")
print(figlet.renderText(input("Input: ")))

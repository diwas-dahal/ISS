import colorama
from colorama import Fore, Style, Back
import re

def cmdMessage(message="", color="white"):
    colorama.init()
    colors = {'white': colorama.Fore.WHITE, 'black': colorama.Fore.BLACK, 'blue': colorama.Fore.BLUE, 'green': colorama.Fore.GREEN, 'magenta': colorama.Fore.MAGENTA, 'yellow': colorama.Fore.YELLOW, 'red': colorama.Fore.RED}
    print(colors[color.lower()], colorama.Style.BRIGHT, message)
    print(colorama.Fore.RESET)

def Errors(message="Coudn't authenticate your data", type="FATAL ERROR"):
    print(colorama.Fore.RED, colorama.Style.BRIGHT)
    print(f"<!----------- {type} ----------------!>")
    print(colorama.Style.BRIGHT, f"{message}")
    print(colorama.Fore.RESET)

def isEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False

from pyfiglet import figlet_format
import random

from Szablon import admire_style, dots_style, cow_style, generate_banner
from Szablon_Task1 import my_own_style


def figlet_style(msg):
    ascii_banner = figlet_format(msg)
    return ascii_banner


def main():
    styles = (dots_style, admire_style, cow_style, my_own_style, figlet_style)
    msg = 'happy coding'
    for style in styles:
        generate_banner(msg, style)


if __name__ == '__main__':
    main()

from cowpy import cow


def generate_banner(msg, style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n')


def dots_style(msg):
    return r"""
..........
. {}  .
. {} .
..........
""".format(msg.capitalize(), ' '.join(msg.split()))


def admire_style(msg):
    return r"""
~~~~~~~~~~
~ {}  ~
~ {} ~
~~~~~~~~~~
""".format(msg.upper(), ' '.join(msg.upper().split()))


def cow_style(msg):
    return cow.milk_random_cow(msg)


def my_own_style(msg):
    modified_msg = msg.replace('_', '~')  # Zamiana znaku "_" na "~"
    modified_msg = modified_msg.upper()  # Zamiana na duże litery
    modified_msg = modified_msg.center(18, '*')  # Wyśrodkowanie i dodanie gwiazdek na bokach
    modified_msg = modified_msg.replace(' ', '-')  # Zamiana spacji na "-"

    return r"""
********************
*                  *
*  {}  *
*                  *
********************
""".format(modified_msg)


def main():
    styles = (dots_style, admire_style, cow_style, my_own_style)
    msg = 'happy coding'
    for style in styles:
        generate_banner(msg, style)


if __name__ == '__main__':
    main()

import colorama

# colorama package basically just enables ANSI in windows command prompt, then directs all print statements to the windows API
# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


print(RED, "This is in red")
print("snd so is this")         # on this line if you don't specify RED, the output will be still red.
                                    # the changes we make to the colors will stay in effect until we cancel them


def colour_print(text: str, *effects: str) -> None:     # *effects, causes all the remaining arguments to be packed into a tuple
    """
    Print `text` using the ANSI sequences to change the color, etc
    :param text: The text to print.
    :param effects: The effect we want. One of the constants
                    defined at the start of this module
    """
    effect_string = "".join(effects)            # effect_string now contains all the ANSI escape sequences that were passed to the function joined into one string
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red in bold", RED, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Blue reverse", BLUE, REVERSE)
colour_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)       # on this line we passed 3 different effects to the function
                                                                                    # arguments- blue, reverse, underline are packed into our effects tuple
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Yellow Bold", YELLOW, BOLD)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()


# python virtual environment
# a python virtual environment contains a copy of your main python installation










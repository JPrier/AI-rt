"""Module providing ASCII art."""


def get_cat_art() -> str:
    """Return a simple cat ASCII art."""
    return r"""
  /\_/\
 ( o.o )
  > ^ <
"""


def get_smiley_art() -> str:
    """Return a simple smiley ASCII art."""
    return r"""
   _____
  /     \
 |  o o  |
 |   ^   |
 |  '-'  |
  \_____/
"""


if __name__ == "__main__":
    print(get_cat_art())

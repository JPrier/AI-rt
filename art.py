"""Utilities for ASCII art."""

CAT_ART = r"""
  /\_/\
 ( o.o )
  > ^ <
"""


def cat_art() -> str:
    """Return ASCII cat art."""
    return CAT_ART.strip("\n")


if __name__ == "__main__":
    print(cat_art())

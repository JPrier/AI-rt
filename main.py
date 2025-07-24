"""Simple greeting module."""


def greet(name: str = "AI-rt", punctuation: str = "!") -> str:
    """Return a friendly greeting.

    Parameters
    ----------
    name:
        Name to greet. Defaults to ``"AI-rt"``.
    punctuation:
        Ending punctuation for the greeting. Defaults to ``"!"``.
    """
    return f"Hello, {name}{punctuation}"


def greet_excited(name: str = "AI-rt") -> str:
    """Return an excited greeting."""
    return f"Wow! Hello, {name}!"


def greet_frank() -> str:
    """Return a friendly greeting for Frank."""
    return greet("Frank")


if __name__ == "__main__":
    print(greet())

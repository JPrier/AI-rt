"""Simple greeting module."""


def greet(name: str = "AI-rt") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def greet_frank() -> str:
    """Return a friendly greeting for Frank."""
    return greet("Frank")


if __name__ == "__main__":
    print(greet())

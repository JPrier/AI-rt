"""Simple greeting module."""


def greet(name: str = "AI-rt") -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())

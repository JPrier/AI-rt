from main import greet, greet_frank, greet_excited


def test_greet_default():
    assert greet() == "Hello, AI-rt!"


def test_greet_custom():
    assert greet("Codex") == "Hello, Codex!"


def test_greet_custom_punctuation():
    assert greet("Codex", punctuation="?") == "Hello, Codex?"


def test_greet_frank():
    assert greet_frank() == "Hello, Frank!"


def test_greet_excited():
    assert greet_excited("Codex") == "Wow! Hello, Codex!"

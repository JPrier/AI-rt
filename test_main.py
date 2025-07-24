from main import greet


def test_greet_default():
    assert greet() == "Hello, AI-rt!"


def test_greet_custom():
    assert greet("Codex") == "Hello, Codex!"

from art import get_cat_art, get_smiley_art


def test_get_cat_art():
    art = get_cat_art()
    assert "/\\_/\\" in art
    assert "( o.o )" in art
    assert "> ^ <" in art


def test_get_smiley_art():
    art = get_smiley_art()
    assert "o o" in art
    assert "^" in art
    assert "-'" in art

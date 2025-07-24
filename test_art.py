from art import get_cat_art


def test_get_cat_art():
    art = get_cat_art()
    assert "/\\_/\\" in art
    assert "( o.o )" in art
    assert "> ^ <" in art

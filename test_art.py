from art import cat_art, CAT_ART


def test_cat_art():
    assert cat_art() == CAT_ART.strip("\n")

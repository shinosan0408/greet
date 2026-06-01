from greet import greet


def test_greet_with_name():
    assert greet("Sho") == "Hello, Sho!"


def test_greet_trims_whitespace():
    assert greet("  Sho  ") == "Hello, Sho!"


def test_greet_empty_falls_back_to_world():
    assert greet("") == "Hello, world!"
    assert greet("   ") == "Hello, world!"

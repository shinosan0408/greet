"""A tiny greeting utility."""


def greet(name):
    """Return a friendly greeting for the given name.

    If the name is empty or only whitespace, greet the world instead.
    """
    name = name.strip()
    if not name:
        return "Hello, world!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    who = sys.argv[1] if len(sys.argv) > 1 else ""
    print(greet(who))

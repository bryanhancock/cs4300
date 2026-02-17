"""Task 2: Variables and Data Types."""


def get_integer() -> int:
    """Return a sample integer."""
    value = 42
    return value


def get_float() -> float:
    """Return a sample floating-point number."""
    value = 3.14
    return value


def get_string() -> str:
    """Return a sample string."""
    value = "Python Programming"
    return value


def get_boolean() -> bool:
    """Return a sample boolean."""
    value = True
    return value


if __name__ == "__main__":
    print(f"Integer : {get_integer()}  -> type: {type(get_integer())}")
    print(f"Float   : {get_float()}    -> type: {type(get_float())}")
    print(f"String  : {get_string()}   -> type: {type(get_string())}")
    print(f"Boolean : {get_boolean()}  -> type: {type(get_boolean())}")

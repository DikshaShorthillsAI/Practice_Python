from math_function import add, subtract

def test_add():
    assert add(2, 3) == 5  # 2 + 3 should be 5
    assert add(-1, 1) == 0  # -1 + 1 should be 0
    assert add(0, 0) == 0   # 0 + 0 should be 0

def test_subtract():
    assert subtract(5, 3) == 2  # 5 - 3 should be 2
    assert subtract(3, 5) == -2  # 3 - 5 should be -2
    assert subtract(0, 0) == 0   # 0 - 0 should be 0

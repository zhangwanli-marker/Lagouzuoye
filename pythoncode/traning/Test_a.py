import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5

if __name__ == '__main__':
    pytest.main(["Test_a.py"])

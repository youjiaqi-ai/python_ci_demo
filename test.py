import pytest

from main import add, multiply, subtract, divide


def test_add():
    """测试加法功能"""
    assert add(3, 5) == 8
    assert add(-2, 2) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_multiply():
    """测试乘法功能"""
    assert multiply(4, 6) == 24
    assert multiply(-3, 5) == -15
    assert multiply(0, 100) == 0
    assert multiply(2.5, 4) == 10.0


def test_subtract():
    """测试减法功能"""
    assert subtract(10, 3) == 7
    assert subtract(5, 8) == -3
    assert subtract(-4, -6) == 2
    assert subtract(3.5, 1.5) == 2.0


def test_divide():
    """测试除法功能"""
    assert divide(10, 2) == 5
    assert divide(-8, 4) == -2
    assert divide(7, 2) == 3.5

    # 测试除数为0的情况
    with pytest.raises(ValueError) as excinfo:
        divide(5, 0)
    assert "除数不能为0" in str(excinfo.value)

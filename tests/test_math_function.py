import pytest
from packages.math_function import add, subtract, multiply, divide

# 正常系
def test_add():
    """
    整数を加算するテスト
    """
    assert add(5, 3) == 8

def test_add_float():
    """
    浮動小数点数を加算するテスト
    """
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract():
    """
    整数を減算するテスト
    """
    assert subtract(5, 3) == 2

def test_subtract_float():
    """
    浮動小数点数を減算するテスト
    """
    assert subtract(0.3, 0.2) == pytest.approx(0.1)

def test_multiply():
    """
    整数を乗算するテスト
    """
    assert multiply(5, 3) == 15

def test_multiply_float():
    """
    浮動小数点数を乗算するテスト
    """
    assert multiply(0.1, 0.2) == pytest.approx(0.02)

def test_divide():
    """
    整数を除算するテスト
    """
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_float():
    """
    浮動小数点数を除算するテスト
    """
    assert divide(0.3, 0.2) == pytest.approx(1.5)
    with pytest.raises(ValueError):
        divide(0.3, 0)

# 異常系
def test_add_string():
    """
    文字列を加算するテスト
    """
    with pytest.raises(TypeError) as e:
        add("5", "3")
    assert str(e.value) == "引数は数値である必要があります"

def test_subtract_string():
    """
    文字列を減算するテスト
    """
    with pytest.raises(TypeError) as e:
        subtract("5", "3")
    assert str(e.value) == "引数は数値である必要があります"

def test_multiply_string():
    """
    文字列を乗算するテスト
    """
    with pytest.raises(TypeError) as e:
        multiply("5", "3")
    assert str(e.value) == "引数は数値である必要があります"

def test_divide_string():
    """
    文字列を除算するテスト
    """
    with pytest.raises(TypeError) as e:
        divide("10", "2")
    assert str(e.value) == "引数は数値である必要があります"
    
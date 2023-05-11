
def add(x, y):
    """
    2つの数値を加算する関数
    :param x: 数値
    :param y: 数値
    :return: x + y
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("引数は数値である必要があります")
    return x + y

def subtract(x, y):
    """
    2つの数値を減算する関数
    :param x: 数値
    :param y: 数値
    :return: x - y
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("引数は数値である必要があります")
    return x - y

def multiply(x, y):
    """
    2つの数値を乗算する関数
    :param x: 数値
    :param y: 数値
    :return: x * y
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("引数は数値である必要があります")
    return x * y

def divide(x, y):
    """
    2つの数値を除算する関数
    :param x: 数値
    :param y: 数値
    :return: x / y
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("引数は数値である必要があります")
    if y == 0:
        raise ValueError("0で割ることはできません")
    return x / y

import pytest
from packages.greeting import hello, goodbye

def test_hello(capsys):
    """
    hello関数のテスト
    """
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello!\n"

def test_goodbye(capsys):
    """
    goodbye関数のテスト
    """
    goodbye()
    captured = capsys.readouterr()
    assert captured.out == "Good-bye!\n"
import pytest
from main import main

test_data = [("racecar", "carrace", True), ("jar", "jam", False)]


@pytest.mark.parametrize("str1, str2, expected", test_data)
def test_main(str1: str, str2: str, expected: bool) -> None:
    is_anagram = main(str1, str2)
    assert is_anagram == expected

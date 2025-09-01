import pytest
from main import main

test_data = [
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
]


@pytest.mark.parametrize("input_array,expected", test_data)
def test_main(input_array: list[int], expected: bool) -> None:
    contains_duplicates = main(input_array)
    assert contains_duplicates == expected

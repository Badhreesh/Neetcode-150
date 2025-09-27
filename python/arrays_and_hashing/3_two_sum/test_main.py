import pytest
from main import two_sum

test_data = [([3, 4, 5, 6], 7, [0, 1]), ([4, 5, 6], 10, [0, 2]), ([5, 5], 10, [0, 1])]


@pytest.mark.parametrize("nums, target, expected", test_data)
def test_two_sum(nums: list[int], target: int, expected: list[int]):
    output = two_sum(nums, target)
    assert output == expected

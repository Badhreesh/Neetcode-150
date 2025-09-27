import pytest
from main import group_anagrams

test_data = [
    (
        ["act", "pots", "tops", "cat", "stop", "hat"],
        [["hat"], ["act", "cat"], ["stop", "pots", "tops"]],
    ),
    (["x"], [["x"]]),
    ([""], [[""]]),
]


@pytest.mark.parametrize("strs, expected", test_data)
def test_group_anagrams(strs: list[str], expected: list[list[str]]):
    output = group_anagrams(strs)
    # Since we don't care about order of inner lists but lists are ordered data types, convert inner lists to a frozenset
    # Since we shouldn't consider the order of the frozensets, convert the main list to a set
    assert set(map(frozenset, output)) == set(map(frozenset, expected))

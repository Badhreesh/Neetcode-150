from collections import defaultdict
from string import ascii_lowercase


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Count the frequency of chars in a word in a tuple and use it as a key in a dict.
    """
    d = defaultdict(list)

    for s in strs:
        count = [0] * len(ascii_lowercase)
        for char in s:
            count[ord(char) - ord("a")] += 1
        d[tuple(count)].append(s)
    result: list[list[str]] = list(d.values())
    return result

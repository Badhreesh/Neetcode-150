# from collections import Counter


def main(str1: str, str2: str) -> bool:
    str1_dict, str2_dict = {}, {}
    for char in str1:
        str1_dict[char] = str1_dict[char] + 1 if char in str1_dict else 1
    for char in str2:
        str2_dict[char] = str2_dict[char] + 1 if char in str2_dict else 1
    return str1_dict == str2_dict
    # return Counter(str1) == Counter(str2) -> Alternate solution

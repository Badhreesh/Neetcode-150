def two_sum(nums: list[int], target: int) -> list[int]:
    """
    To get the solution using a single pass of the array, check if the difference between target and current num
    exists in a dict (dict lookups are always constant)
    """
    seen = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], idx]
        seen[num] = idx
    return []

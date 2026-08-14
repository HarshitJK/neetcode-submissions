class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        result = set(nums)
        if len(result) != length:
            return True
        else:
            return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = set()
        for i in nums:
            if i in unique_numbers:
                return True
            unique_numbers.add(i)
        return False

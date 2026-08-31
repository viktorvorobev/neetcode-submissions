class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_set = set()
        for num in nums:
            if num in test_set:
                return True
            test_set.add(num)
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in targets:
                return list((targets[pair], i))
            targets[num] = i
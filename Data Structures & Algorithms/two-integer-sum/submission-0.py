class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_sum = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in prev_sum:
                return [prev_sum[pair], i]
            prev_sum[num] = i
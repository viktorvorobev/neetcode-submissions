class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            attempt_index = (left + right) // 2
            attempt_val = nums[attempt_index]
            if attempt_val == target:
                return attempt_index
            if attempt_val > target:
                right = attempt_index - 1
            else:
                left = attempt_index + 1
        return -1
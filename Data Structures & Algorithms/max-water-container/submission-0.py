class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0
        while left < right:
            distance = right - left
            if heights[left] <= heights[right]:
                min_height = heights[left]
                left += 1
            else:
                min_height = heights[right]
                right -= 1
            volume = min_height * distance
            max_volume = max(max_volume, volume)
        return max_volume
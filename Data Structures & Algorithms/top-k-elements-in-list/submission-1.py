class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        keys_by_frequency = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
        return keys_by_frequency[0:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        sorted_pairs = sorted(counter.items(), key=lambda i: i[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_pairs[i][0])
        return result

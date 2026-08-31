class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count = [0] * len(range(ord('a'), ord('z') + 1))
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            hashable_count = tuple(count)
            if hashable_count in anagrams:
                anagrams[hashable_count].append(string)
            else:
                anagrams[hashable_count] = [string]
        return list(anagrams.values())
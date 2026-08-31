class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        freq_t = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for letter in s:
            freq_s[letter] += 1
        for letter in t:
            freq_t[letter] += 1
        return freq_s == freq_t
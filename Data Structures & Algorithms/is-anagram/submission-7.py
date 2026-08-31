class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters_freq = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}
        
        for i in range(len(s)):
            letters_freq[s[i]] += 1
            letters_freq[t[i]] -= 1
        for count in letters_freq.values():
            if count != 0:
                return False

        return True
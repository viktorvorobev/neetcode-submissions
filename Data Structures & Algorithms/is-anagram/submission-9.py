class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0]*26
        for i in range(len(s)):
            counter[ord('a') - ord(s[i])] += 1
            counter[ord('a') - ord(t[i])] -= 1
        for val in counter:
            if val != 0:
                return False
        return True
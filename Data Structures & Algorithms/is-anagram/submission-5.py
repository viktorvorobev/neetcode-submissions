class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for char in s:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
        for char in t:
            if char not in characters:
                return False
            characters[char] -= 1
        for count in characters.values():
            if count != 0:
                return False
        return True
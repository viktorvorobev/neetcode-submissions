class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        for letter in t:
            if letter in letter_count:
                letter_count[letter] -= 1
                if letter_count[letter] == 0:
                    letter_count.pop(letter, None)
            else:
                return False
        return not letter_count
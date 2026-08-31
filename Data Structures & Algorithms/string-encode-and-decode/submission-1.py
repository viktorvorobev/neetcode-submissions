class Solution:
    DELIMITER = "#"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + self.DELIMITER + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        word_len_str = ""

        i = 0
        while i < len(s):
            if s[i] == self.DELIMITER:
                word_len = int(word_len_str)
                start = i + 1
                end = start + word_len
                res.append(s[start:end])

                i = end
                word_len_str = ""
                continue

            word_len_str += s[i]
            i += 1
        return res
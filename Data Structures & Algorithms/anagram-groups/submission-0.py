import json
import hashlib

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, List[str]] = {}

        for s in strs:
            s_counter: dict[str, int] = {}
            for char in s:
                if char in s_counter:
                    s_counter[char] += 1
                else:
                    s_counter[char] = 1
            counter_hash = hashlib.sha256(json.dumps(s_counter, sort_keys=True).encode()).hexdigest()
            if counter_hash in anagrams:
                anagrams[counter_hash].append(s)
            else:
                anagrams[counter_hash] = [s]
        return list(anagrams.values())

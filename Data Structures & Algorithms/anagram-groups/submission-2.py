from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have a dictonary of where the key is the counter and the value is the list
        groupAnagrams = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                letters[index] += 1
            groupAnagrams[tuple(letters)].append(s)
        res = []
        for value in groupAnagrams.values():
            res.append(list(value))
        return res
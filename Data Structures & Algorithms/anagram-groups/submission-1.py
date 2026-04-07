from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap as key index as value
        # {counter : index}
        # [[0fkrf]]
        # iterate through each word
        # check if counter is in the hashmap
        
        hashmap = defaultdict(list) # (counter, index)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        return hashmap.values()
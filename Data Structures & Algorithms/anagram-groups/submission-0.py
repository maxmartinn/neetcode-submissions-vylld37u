from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap as key index as value
        # {counter : index}
        # [[0fkrf]]
        # iterate through each word
        # check if counter is in the hashmap
        
        res = []
        hashmap = {} # (counter, index)
        
        for s in strs:
            count = tuple(sorted(s))
            if count in hashmap:
                res[hashmap[count]].append(s)
            else:
                hashmap[count] = len(res)
                res.append([s])
        return res
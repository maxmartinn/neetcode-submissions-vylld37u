from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have a dictonary of where the key is the counter and the value is the list
        i = 0
        j = 1

        res = dict()

        while i < len(strs):
            tupleStr = tuple(sorted(strs[i]))
            if not tupleStr in res:
                res[tupleStr] = []
            res[tupleStr].append(strs[i])
            i += 1
            
        return res.values()

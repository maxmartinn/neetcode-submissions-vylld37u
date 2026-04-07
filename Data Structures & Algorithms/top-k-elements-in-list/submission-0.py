class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap with keys (freq, [int])
        # iterate between length of nums and see if the freq is in the hashmap
        # when the res size is equal to k return the res

        freqCount = defaultdict(list) # {1 : {1} 2: {2}, 3: {3}}
        inFreqCount = defaultdict(int) # {1: 1, 2: 2, 3: 1}
        res = []
        for n in nums:
            if n not in inFreqCount:
                freqCount[1].append(n)
                inFreqCount[n] = 1
            else:
                freqCount[inFreqCount[n]].remove(n)
                freqCount[inFreqCount[n] + 1].append(n)
                inFreqCount[n] = inFreqCount[n] + 1

        for freq in range(len(nums), -1, -1):
            if len(freqCount[freq]) > 0:
                for n in freqCount[freq]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return None
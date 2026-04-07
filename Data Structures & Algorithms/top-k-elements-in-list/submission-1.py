class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqMap {value: freq}
        # freqArray {freq, set} equal to len of nums
        
        # iterate through nums
        # check the valeu in freqMap
        # go to that freqIndex and remove the value and add it to the freqIndex += 1

        freqMap = dict()

        freqArray = [set() for _ in range(len(nums) + 1)]

        res = []

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
            freq = freqMap[n]
            if n in freqArray[freq - 1]:
                freqArray[freq-1].remove(n)
            freqArray[freq].add(n)
        print(freqArray)

        for resSet in freqArray[::-1]:
            for element in resSet:
                res.append(element)
                if len(res) == k:
                    return res

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarification 

        # given a list of numbers, return k most frequent numbers in the array

        # brute force

        """
        for each unique value in nums, count the frequency and store pair in a list

        reverse sort the list and select first k values
        """

        # optimal solution

        # instead of sorting the list to retrieve first k values, i can use bucket sort to retrieve numbers in reverse order

        #

        """
        planning 
        the freqMap repersents a current number frequency at any given time

        the bucketSort is a list of sets where the index repersents current frrqeucny of a number

        freqMap and bucketSort are both defined

        iterate between each value in nums:
            add one to the value of the current number in freqMap
            update index in bucketSort so the current index of the current value is in the updated spot
        
        iterate in reverse order and stop when the length of result is equal to 
        """

        res = []
        freqMap = Counter(nums)
        bucketSort = [[] for _ in range(len(nums) + 1)]
        for key, value in freqMap.items():
            bucketSort[value].append(key)
        for i in range((len(nums)), -1, -1):
            for n in bucketSort[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res


        """

        Input: nums = [1,2,2,3,3,3], k = 2

        Output: [2,3]

        freqMap = {1: 1, 2: 2, 3: 3}
        bucketSort = [[] [1] [2] [3] [] [] []]
        res = [3, 2]
        """
            
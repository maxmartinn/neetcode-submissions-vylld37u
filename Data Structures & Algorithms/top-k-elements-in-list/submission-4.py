class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarification 

        # given a list of numbers, return k most frequent numbers in the array

        # brute force

        """
        for each unique value in nums, count the frequency and store pair in a list

        reverse sort the list and select first k values
        """

        unique_list = set(nums)

        res_list = []

        for n in unique_list:
            count = 0
            for x in nums:
                if x == n:
                    count += 1
            res_list.append((n, count))
        res_list.sort(key=lambda x: x[1], reverse=True)
        return [x for x, _ in res_list[:k]]

            
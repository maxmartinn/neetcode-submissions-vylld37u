class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        clarification
        given a string s, find the length of the longest substring with out repeated characters

        example:

        input: xyzaz

        output 4

        naive solution:

        iterate for every combination of substrings and see if there if its the longest substring without repeating characters


        optimize:

        this solutions causes there to be a lot of repeated work

        because everry combination of substring is made

        reduce repeated work by using a sliding window

        while the current window does not contain any duplicates increase the window, while it does decrease the size of the window


        plan:

        create a sliding window using left and right pointers as well as a set

        # increase right pointer while the right value does not exist in the set

        # decrease left pointer and remove left value from set while right value is in the set

        # at each iteration update the result to be the maximum of the result or the set


        # set = {y, z, x}
        # res = 3
        Input: s = "zxyz"
        #             l
        #                r
        Output: 3
        """

        strSet = set()
        res = 0
        l = 0
        r = 0

        while r < len(s):
            while s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            strSet.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res

        """
        # set = {x, y, z}
        # res = 3
        Input: s = "zxyz"
        #            l
        #                r
        Output: 3
        """
    


        
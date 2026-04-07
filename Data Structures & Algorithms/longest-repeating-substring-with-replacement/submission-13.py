class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Question notes:

        given string s

        consists of only uppercase english letters (dont need to worry about cases)

        and integer k

        choose up to k characters to replace in the string with any uppercase enlgish character

        after preforming k replaces return the length of the longest substring

        naive solution:

        iterate to find every substring

        find the most frequent occuring characters

        find if the string can be repeating by subtracting length of string and k seing if this result is greater or equal to the length of the string

        solution would be O(n^2) time and O(n) space

        optimize solution:

        optimize using a sliding window

        plan:

        define window hashmap contain the character counts

        start each pointer at l and r at 0

        define res at 0

        iterate while r is less than the length of s

        keep track of the character that occurs the most

        update max_freq_char when incresing array, checking if the newly added value is equal to the max occuring character

        while decrementing, max occuring character will remain the same as new max window size can be created while decrementing array 

        move left and right pointers based on if the current window is valid

        increment right pointer if current window is valid with replacement, adding the right value to the window

        while window is not valid increment the left pointer, decrementing it from the window


        """

        l, r, res = 0, 0, 0
        window = defaultdict(int) # {character : 0}
        max_freq = 0
        while r < len(s):
            window[s[r]] += 1
            max_freq = max(max_freq, window[s[r]])
            while r - l + 1 - max_freq > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
        """
        Input: s = "XYYXZ", k = 2
                     l
                        r
        Output: 4

        s = "XYYXZ"

        window = {X: 2, Y : 1, Z : 1}
        l = 1
        r = 4
        max_freq = Y
        res = 0
        """ 








class Solution:
    def isPalindrome(self, s: str) -> bool:
        # restate

        # return true if the string prvoided is a palindrome and return false if the string is not a palindrome
        
        # in order for a string to be considered a palindrome the string is case insensitive and ignores all non alphanumeric characters

        # brute force:

        # using two pointers starting from the start and end of the array, check if the current pointers are alphanumeric and the same character case insensitive

        # shift pointers respectively

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
                
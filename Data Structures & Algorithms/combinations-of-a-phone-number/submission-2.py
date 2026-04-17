class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        if not digits:
            return res
        def backtrack(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for c in digitMap[digits[i]]:
                backtrack(i + 1, curr + c)
        backtrack(0, "")
        return res
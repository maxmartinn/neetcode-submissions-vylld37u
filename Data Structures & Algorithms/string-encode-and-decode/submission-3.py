class Solution:
    # have a delimeter to encode and decode the string

    # first encode then decode
    def encode(self, strs: List[str]) -> str:
        # have the count of how many characters are to the right of it then a pound sign

        # 4#neet4#code4#love4#you
        res = []
        for s in strs:
            n = len(s)
            res.append(str(n) + "#" + s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:

        # have a running count of how long the 
        res = []
        j = 0

        # 4#neet4#code4#love4#you

        # check if current character is a number
        # add to count
        i = 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
         
        return res
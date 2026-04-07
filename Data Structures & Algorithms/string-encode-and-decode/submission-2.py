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
        count = 0

        # 4#neet4#code4#love4#you

        # check if current character is a number
        # add to count
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                count *= 10
                count += int(s[i])
                i = i + 1
            else:
                res.append(s[i + 1:i + count + 1]) 
                i = i + count + 1
                count = 0
         
        return res
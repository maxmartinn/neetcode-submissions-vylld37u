class Solution:
    # 5#abcde4#abcd3#abc
    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += (str(len(w)) + '#' + w)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while str(s[j]) != "#":
                j += 1
            encodedLength = int(s[i:j])
            res.append(s[j+1:encodedLength+j+1])  
            i = encodedLength + j + 1   
        print(res)    
        return res

        
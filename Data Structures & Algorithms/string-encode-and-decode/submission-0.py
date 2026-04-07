class Solution:
    # 5#abcde4#abcd3#abc
    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += (str(len(w)) + '#' + w)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs = []
        decodeLength = ""
        decodeRemaning = 0
        i = 0
        while i < len(s):
            while s[i] != "#" and not decodeRemaning:
                decodeLength += s[i]
                i += 1
            print(decodeLength)
            decodeRemaning = int(decodeLength) + i
            decodeLength = ""
            w = ""
            while i < decodeRemaning:
                w += s[i+1]
                i += 1
            strs.append(w)
            i += 1
            decodeRemaning = 0
            print(strs)
        return strs

            

        return strs
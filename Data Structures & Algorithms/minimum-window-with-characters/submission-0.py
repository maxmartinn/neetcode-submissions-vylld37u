class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # have increase window untill the substring of s contains all letters of t

        # decrease window untill the substring of s does not contain all letters of t, add value to the result

        # naive:

        # iterate through all possible substring and see if it contains every character in t

        # optimal

        # using a map to count all characters in t and a matched varaible, if matched is equal to all the unique character in t then it is possible and compare with current res

        # if adding one to s_count makes that value equal to the value in t_count increase match by 1
        # if decrementing one to s_count makes that value 1 less than to the value in t_count decrease match by 1
        matched = 0

        s_count = defaultdict(int)
        t_count = Counter(t)

        l = 0
        r = 0
        res = ""
        while r < len(s):
            s_count[s[r]] += 1
            if s_count[s[r]] == t_count[s[r]]:
                matched += 1
            while matched == len(t_count):
                print(s[l:r+1])
                new_word = s[l:r+1]
                res = new_word if len(res) > len(new_word) or res == "" else res
                s_count[s[l]] -= 1
                if s_count[s[l]] == t_count[s[l]] - 1:
                    matched -= 1
                l += 1
            r += 1
        return res
        """

        Input: s = "OUZODYXAZV", t = "XYZ"
                          l 
                              r
        Output: "YXAZ"
        res = "YXAZ"
        t_count = {X : 1, Y : 1, Z : 1}
        s_count = {O : 1 D : 0 Y : 0 X : 1, A : 1, Z: 1 V : 1}
        matched = 2
        """
        

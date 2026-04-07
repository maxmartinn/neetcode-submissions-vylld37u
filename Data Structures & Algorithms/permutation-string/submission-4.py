class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have a window size of s1, check all window sizes starting from len(s1) to the end of the array

        window_s1 = defaultdict(int)
        window_s2 = defaultdict(int)
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            window_s1[s1[i]] += 1
            window_s2[s2[i]] += 1
        

        if window_s1 == window_s2:
            return True

        for i in range(len(s1), len(s2)):
            window_s2[s2[i - len(s1)]] -= 1
            if window_s2[s2[i - len(s1)]] == 0:
                del window_s2[s2[i - len(s1)]]
            window_s2[s2[i]] += 1
            
            print(window_s1, window_s2)
            
            if window_s1 == window_s2:
                return True
        return False

        """

        Input: s1 = "abc", s2 = "lecabee"

        window_s1 = {a : 1 b : 1 c : 1}
        window_s2 = {l : 0 e : 0 c : 1, a : 1, b : 1}

        i = 4
        Output: true
        """
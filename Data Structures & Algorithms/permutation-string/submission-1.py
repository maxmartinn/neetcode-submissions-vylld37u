class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # have sliding window set 
        # remove left pointer when
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        for c in s1:
            index = ord(c) - ord("a")
            s1Count[index] += 1
        matchCount = 0
        l, r = 0, 0
        while r < len(s2):
            rightChar = s2[r]
            rightIndex = ord(rightChar) - ord("a")
            s2Count[rightIndex] += 1
            matchCount = 0
            for index in range(len(s1Count)):
                if s1Count[index] == s2Count[index]:
                    matchCount += 1
            if matchCount == 26:
                return True
            if r - l + 1 == len(s1):
                leftChar = s2[l]
                leftIndex = ord(leftChar) - ord("a")
                s2Count[leftIndex] -= 1
                l += 1
            print(s2Count)
            r += 1
        return False
                
            
        
        return False

                
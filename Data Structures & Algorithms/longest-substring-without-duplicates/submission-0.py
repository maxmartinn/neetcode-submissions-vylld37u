class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # make res
      res = 0
      # create character set
      characterSet = set()
      # make left pointer
      l = 0
      # iterate through all characters in s
      for r in range(len(s)):
      # check if current character is in character set
        while s[r] in characterSet:
      # if character in set:
            popLeft = s[l]
            characterSet.remove(popLeft)
            l += 1
      # make a while loop to window popleft and remove from character set 
      # res equals the max of current res and length of substring
        characterSet.add(s[r])
        res = max(res, r - l + 1)
      # add current character to set
      return res
    

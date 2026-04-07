class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # restate problem
        # example
        # mention brute force
        # say optimal algorithims to use
        # dry run 

        # group all anagrams together into sublists

        # ["abc", "bca", bat]

        # res = [["abc", "bca"], ["bat"]]

        # brute force solution:

        # have a map storing anagrams as sorted strings

        # {"abc": []}

        # return values

        # iterating through all words:
            # sorted current word and add to map

        # return map as array dropping keys


        # optimal solution

        """
        have a map storing anagrams as tuples

        iterate through all words
            get the count of current word and store in map as tupple
        
        reutrn map as array dropping keys 
        """

        strMap = defaultdict(list)

        for w in strs:
            wCount = [0 for _ in range(26)]
            for c in w:
                wCount[ord(c) - ord('a')] += 1
            strMap[tuple(wCount)].append(w)
        return list(strMap.values())


        # ["abc", "bca", baz]

        # strMap = {(1 1 1 .. 0) : ["abc", "bca"], [1 1 0 0 ...... 0 1]: ["baz"]}
        # wCount = [1 1 0 0 ...... 0 1]
        # res = [["abc", "bca"], ["baz"]]

        # n is length of list
        # m is legnth of longest word
        # Time Complexity: O(m * n)
        # Space complexity: O(n)





            
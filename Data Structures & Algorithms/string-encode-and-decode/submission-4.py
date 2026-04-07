# can i use any character to encode and decode

# so for example: w "He llo" "World"  will be encoded into a single string such as "He lloWorld" then decoded back into "He llo" "World"

"""
plan

encode: find a way to add a delimter in between each word in the list so that the decoder can code it

decode: decode the encoded string into a list of strings so that the result is returned as the original list of strings

encode:

given a word, the function will add the word to the result such as

[Hello, World]

[DELIMETER]Hello[DELIMETER]World

Having a delimeter before each word gives the function an opportunity to process the next word

The delimeter that provides best use if it starts off with a number for how long the word is and a symbol to dicate that the number has stopped

For example:

encoded string 5!Hello5!World

decoded string as list [Hello, World]

Decode:

    given the encoded string the decode function can decode the string to return as a list

    have a result of list

    iterate through the encoded string
        start off by counting untill the symbol is located, from the start index to the current index, that is how large the word is
        add the word to the list and update pointers to correct spots

    



"""



class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + "!" + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j += 1
            num = int(s[i : j])
            res.append(s[j + 1: j + 1 + num])
            i = j + num + 1
        return res
    
    # Hello, World

    # 5!Hello5!World
    # i = 0
    # j = 1
    # num = 5
    # res = []
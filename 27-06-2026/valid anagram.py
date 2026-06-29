# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def isanagram(s:str,t:str)->bool:
    if len(s) != len(t):
        return False

    h = {}

    for char in s:
        h[char] = h.get(char,0) + 1

    for char in t:
        if char not in h:
            return False

        h[char] -= 1

        if h[char] < 0:
            return False

    return True

print(isanagram("rang","gnra"))

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.

# Follow up: Can you solve it in O(n) time and O(1) space?

# using stack is best option here
# first we push and pop when got # and then add
# then compare both string


# O(n) space complexity cuz stack
def backspaceString(s: str, t: str) -> bool:
    def build(text: str) -> str:
        stack = []

        for ch in text:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

    return build(s) == build(t)


# only used the two pointer for space complexity O(1)
def backspaceStringOpti(s: str, t: str) -> bool:
    def getvalidindex(st: str, end: int):
        count_backspace = 0
        while end >= 0:
            if st[end] == "#":
                count_backspace += 1
            elif count_backspace > 0:
                count_backspace -= 1
            else:
                break
            end -= 1

        return end

    ps = len(s) - 1
    pt = len(t) - 1

    while ps >= 0 or pt >= 0:
        ps = getvalidindex(s, ps)
        pt = getvalidindex(t, pt)
        if ps < 0 and pt < 0:
            return True
        if ps < 0 or pt < 0:
            return False
        elif s[ps] != t[pt]:
            return False
        ps -= 1
        pt -= 1

    return True


print(backspaceStringOpti("ab#c##", "c#d#"))

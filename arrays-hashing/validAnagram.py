from collections import Counter
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10e4
# s and t consist of lowercase English letters.

# O(n log n)
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    if sorted(s) == sorted(t):
        return True
    else:
        return False

# O(n)
def isAnagramNotVanilla(s, t):
    return len(s) == len(t) and Counter(s) == Counter(t)

print(isAnagramNotVanilla("anagram", "nagaram"))
print(isAnagram("anagram", "nagaram"))
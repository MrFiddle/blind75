# We need to keep track of ALL the substring
# We need to keep track of the characters that the current substring that we are working on has
# We need to make it work:D (optimization is optional ig)

def lengthOfLongestSubstring(s):

    substrings = []
    cache = []
    # print(s)

    for i in range(len(s)):
        if s[i] not in cache:
            cache.append(s[i])
        else:
            new_substring = ''.join(cache)
            substrings.append(new_substring)
            cache.clear()
            cache.append(s[i])
    
    substrings.append(cache)

    print(cache)
    print(substrings)
    return(len(max(substrings, key=len)))


initial_string = 'dvdf'
print(lengthOfLongestSubstring(initial_string))
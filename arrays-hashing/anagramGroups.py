from collections import defaultdict

def anagramGroups(words):
  # Create a dictionary with default values as empty lists
  hashMap = defaultdict(list)

  # Iterate through each word in the input list
  for i in words:
    # Sort the characters in the word and join them back into a string
    sortedWord = ''.join(sorted(i))
    
    # Append the word to the list corresponding to its sorted version in the dictionary
    hashMap[sortedWord].append(i)
  
  # Return a list of all the values in the dictionary
  return list(hashMap.values())


# Test case
words = ["eat","tea","tan","ate","nat","bat"]
print(anagramGroups(words))
# Check anagrams using sorted()

def anagram_sort(text1, text2):

    return sorted(text1) == sorted(text2)


print(anagram_sort("silent", "listen"))

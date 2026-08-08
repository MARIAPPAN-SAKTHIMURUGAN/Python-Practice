from collections import Counter


def anagrams_counter(text1, text2):

    return Counter(text1) == Counter(text2)


print(anagrams_counter("silent", "listen"))

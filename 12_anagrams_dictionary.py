# Check anagrams using dictionaries

def anagrams(text1, text2):

    frequency1 = {}
    frequency2 = {}

    for ch in text1:

        if ch in frequency1:
            frequency1[ch] += 1
        else:
            frequency1[ch] = 1

    for ch in text2:

        if ch in frequency2:
            frequency2[ch] += 1
        else:
            frequency2[ch] = 1

    return frequency1 == frequency2


print(anagrams("silent", "listen"))

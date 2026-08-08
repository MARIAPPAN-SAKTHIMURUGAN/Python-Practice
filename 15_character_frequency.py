# Count the frequency of each character

def character_frequency(text):

    frequency = {}

    for ch in text:

        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency


text = "programming"

print(character_frequency(text))

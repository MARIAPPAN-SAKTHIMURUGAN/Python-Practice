def palindrome(text):
    return text == text[::-1]

word = "madam"

if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")

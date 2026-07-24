def reverseString(word):
    print("Before reverse ---" + word)
    stack = []
    for char in word:
        stack.append(char)
    reverse_word=""
    while stack:
        reverse_word+=stack.pop()
    print("After reverse ---")
    return reverse_word
    
print(reverseString("CAT") )
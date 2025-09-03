
def unique_words(word):
    stack = []
    for character in word:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    return stack if stack else "Empty String"

print(unique_words("aab"))



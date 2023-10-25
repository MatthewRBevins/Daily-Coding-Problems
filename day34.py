
def is_palindrome(word):
    # Reverse word
    if word[::-1] == word:
        return True
    return False

def find_palindrome(orig, word):
    if len(word) > len(orig)*2:
        return orig + orig
    if is_palindrome(word):
        hi.append(word)
        return word
    best = orig + orig
    for index, val in enumerate(word):
        word = word[0:index] + word[len(word)-index-1] + word[index:len(word)]
        thistry = find_palindrome(orig, word)
        if len(best) > len(thistry):
            best = thistry
    return best


print(find_palindrome("race", "race"))
print(find_palindrome("google", "google"))

def censor_words(text, banned_word):
    return text.replace(banned_word, "***")
    pass
text = "the cat sat on the cat mat"
banned_word = "cat"

print(censor_words(text, banned_word))
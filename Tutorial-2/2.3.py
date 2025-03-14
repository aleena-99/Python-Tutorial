
def remove_words(s, words):
    for word in words:
        s = s.replace(word, "")
    return s.strip()

print(remove_words("Hello world, welcome to Python", ["world", "Python"]))

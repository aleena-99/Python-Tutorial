def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

print(remove_vowels("Hello World"))

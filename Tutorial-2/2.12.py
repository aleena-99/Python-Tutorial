def replace_spaces(s):
    return s.replace(" ", "*") if " " in s else f"${s}$"

print(replace_spaces("Hello World"))
print(replace_spaces("Python"))

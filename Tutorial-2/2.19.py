import re

def is_valid_password(pwd):
    return (len(pwd) >= 6 and 
            any(c.islower() for c in pwd) and 
            any(c.isupper() for c in pwd) and 
            any(c.isdigit() for c in pwd) and 
            any(c in "$#@" for c in pwd))

print(is_valid_password("Hello@1"))

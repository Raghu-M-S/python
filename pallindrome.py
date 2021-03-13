import string
def is_palindrome(s):
    s=s.lower()
    s=s.replace(" ","")

    return s==s[ : : -1]

s1="racecar"
print(is_palindrome(s1))

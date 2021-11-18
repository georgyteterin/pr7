def is_palindrome(s):
    if len(s) in [0, 1]:
        return True
    elif s[0] == s[-1]:
        s2 = s[1:-1]
        return is_palindrome(s2)
    else:
        return False
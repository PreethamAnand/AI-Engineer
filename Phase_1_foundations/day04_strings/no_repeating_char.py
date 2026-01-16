def no_rep(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None


def no_spaces(a):
    a = a.replace(" ","")
    return no_rep(a)
a = input("Enter string:")
print("Non-repeating character string:", no_spaces(a))

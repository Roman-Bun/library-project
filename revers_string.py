def revers_string(s):
    n = ""
    left, right = 0, len(s) - 1
    while left < len(s):
        n += (s[right])
        left += 1
        right -= 1
    return n

print(revers_string("hello"))
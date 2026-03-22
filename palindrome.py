# Спосіб 3
# def is_palindrome(s):
#     for i in range(len(s) // 2):
#         if s[i] != s[-i - 1]:
#             return False
#     return True

# Спосіб 1 — Python магія (найпростіший):
# def is_palindrome(s):
#    return s == s[::-1]  # s[::-1] — рядок навпаки

# Спосіб 2 — два вказівники (класичний алгоритм):
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

words = ["racecar", "hello", "madam"]
for word in words:
    result = "паліндром" if is_palindrome(word) else "НЕ паліндром"
    print(f"{word} — {result}")
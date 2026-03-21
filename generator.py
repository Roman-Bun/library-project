def squares(n):
    for i in range (1, n+1):
        yield i ** 2

gen = squares(5)

print(next(gen))
print(next(gen))
print(next(gen))

for num in squares(7):
    print(num)
def find_duplicates(nums):
    seen = set()
    duplicates =set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

num = [1, 2, 3, 2, 4, 3, 5]

print(find_duplicates(num))
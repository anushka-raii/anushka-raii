# Count Frequency of Elements

nums = [2, 3, 2, 5, 3, 2, 5, 5, 5, 3]

frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)

from collections import Counter

S = input().strip()

count = Counter(S)
answer = None
max_count = 0
for char, num in count.items():
    if num > max_count:
        answer = char
        max_count = num
    elif num == max_count and char < answer:
        answer = char
print(answer)
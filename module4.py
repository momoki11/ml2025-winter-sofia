n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
x = int(input())
if x in numbers:
    print(numbers.index(x) + 1)
else:
    print(-1)

import sys

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

numbers = [i for i in range(2, n + 1)]
results = []
while(len(numbers) > 0):
    count = 1
    target_number = numbers.pop(0)
    results.append(target_number)
    while(target_number * count <= n):
        try:
            numbers.remove(target_number * count)
        except ValueError:
            pass
        else:
            results.append(target_number * count)
        count += 1
print(results[k - 1])
import sys

count = int(sys.stdin.readline())
numbers = sys.stdin.readline()
numbers = numbers.split()

original_numbers = []
for x in range(count):
    original_numbers.append((int(numbers[x]), x))
sorted_numbers = sorted(original_numbers)

results = ''
for x in original_numbers:
    results += str(sorted_numbers.index(x))
    results += ' '
results = results[:-1]
print(results)
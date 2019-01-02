import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

squares = [x * x for x in range(1, 101)]
square_sum = 0
results = []
# M <= square <= N
for i in range(100):
    if m <= squares[i] <= n:
        results.append(squares[i])

if len(results) > 0:
    print(sum(results))
    print(results[0])
else:
    print(-1)
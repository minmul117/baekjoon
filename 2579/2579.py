import sys

t = int(sys.stdin.readline())
stair_scores = []

for i in range(t):
    stair_scores.append(int(sys.stdin.readline()))

stair_sums = {}
def sum_of_stairs(n):
    if n == 1:
        return stair_scores[0]
    elif n == 2:
        return stair_scores[0] + stair_scores[1]
    elif n == 3:
        return max(stair_scores[2] + stair_scores[1],
                   stair_scores[2] + stair_scores[0])
    else:
        try:
            return stair_sums[n]
        except KeyError:
            stair_sums[n] = max(sum_of_stairs(n - 2) + stair_scores[n - 1],
                                sum_of_stairs(n - 3) + stair_scores[n - 1] + stair_scores[n - 2])
            return stair_sums[n]
print(sum_of_stairs(t))
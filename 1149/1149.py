# test

import sys

n = int(sys.stdin.readline())

rgb_cost = []
for i in range(n):
    cost_str = sys.stdin.readline().split()
    rgb_cost.append(tuple(map(int, cost_str)))

results = {}

results[1] = rgb_cost[0]
def get_results(num):
    try:
        return results[num]
    except KeyError:
        pass

    prev_results = get_results(num - 1)
    cur_rgb = rgb_cost[num - 1]
    cur_results = (min(cur_rgb[0] + prev_results[1], cur_rgb[0] + prev_results[2]),
                   min(cur_rgb[1] + prev_results[0], cur_rgb[1] + prev_results[2]),
                   min(cur_rgb[2] + prev_results[0], cur_rgb[2] + prev_results[1]))
    results[num] = cur_results
    return cur_results

print(min(get_results(n)))
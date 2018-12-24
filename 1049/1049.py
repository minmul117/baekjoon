import sys
from operator import itemgetter

line = sys.stdin.readline().split()
guitar_strings = int(line[0])
company_counts = int(line[1])

bundle_count = int(guitar_strings / 6)
one_count = guitar_strings % 6

price_lists = []
for x in range(company_counts):
    values = sys.stdin.readline().split()
    price_lists.append((int(values[0]), int(values[1])))

price_lists.sort(key=itemgetter(0))
bundle_price = price_lists[0][0]
price_lists.sort(key=itemgetter(1))
one_price = price_lists[0][1]

if bundle_price > one_price * 6:
    bundle_price = one_price * 6

print(bundle_count * bundle_price + min(one_count * one_price, bundle_price)) 
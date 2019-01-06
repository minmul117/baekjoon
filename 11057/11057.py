import sys

n = int(sys.stdin.readline())
temp_list = []
result = 0

if n == 1:
    print(10)
else:
    result = 0
    temp_list = [1] * 10
    for i in range(n):
        result = sum(temp_list)
        temp_list_2 = []
        temp_list_2.append(result)
        for j in range(1, 10):
            temp_list_2.append(temp_list_2[j - 1] - temp_list[j - 1])
        temp_list = temp_list_2
    print(result % 10007)
max_count = 10000
result_set = set()

def get_self_number(n):
    result = n
    remainder = n
    for i in range(4):
        result += remainder % 10
        remainder = int(remainder / 10)
    return result

def self_number():
    for i in range(1, max_count):
        result_set.add(i)
    for i in range(1, max_count):        
        result = get_self_number(i)
        if result in result_set:
            result_set.remove(result)
    for __, element in enumerate(result_set):
        print(element)

self_number()

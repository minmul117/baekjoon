import sys

class Stack(object):
    elements = None
    count = None

    def __init__(self):
        self.elements = []
        self.count = 0

    def push(self, number, result):
        self.elements.append(number)
        result.append('+')
        self.count += 1

    def pop(self, result):
        if self.count <= 0:
            return -1
        else:
            self.count -= 1
            result.append('-')
            return self.elements.pop()
    
    def top(self):
        if self.count <= 0:
            return -1
        else:
            return self.elements[self.count - 1]

count = int(sys.stdin.readline())
number_pool = [i for i in range(1, count + 1)]
stack = Stack()
sequences = []
for __ in range(count):
    number = int(sys.stdin.readline())
    sequences.append(number)

results = []
failed = False

def add_numbers(pool, results):
    number = pool[0]
    while number <= sequence:
        stack.push(number, results)
        if len(pool) > 0:
            pool.pop(0)
            try:
                number = pool[0]
            except IndexError:
                break

for sequence in sequences:
    top = stack.top()
    if top != -1:
        if top == sequence:
            stack.pop(results)
        else:
            if sequence < top:
                print('NO')
                failed = True
                break
            else:
                add_numbers(number_pool, results)
                stack.pop(results)
    else:
        add_numbers(number_pool, results)
        stack.pop(results)

if not failed:
    for result in results:
        print(result)
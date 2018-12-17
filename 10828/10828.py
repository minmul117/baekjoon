import sys


class Stack:
    elements = []
    count = 0

    def process_command(self, args):
        if args[0] == 'push':
            element = int(args[1])
            self.elements.append(element)
            self.count += 1
        elif args[0] == 'pop':
            if self.count <= 0:
                print(-1)
            else:
                popped_item = self.elements.pop()
                self.count -= 1
                print(popped_item)
        elif args[0] == 'size':
            print(self.count)
        elif args[0] == 'empty':
            if self.count == 0:
                print(1)
            else:
                print(0)
        elif args[0] == 'top':
            if self.count <= 0:
                print(-1)
            else:
                print(self.elements[self.count - 1])

max_count = sys.stdin.readline()
stack = Stack()
for i in range(int(max_count)):
    raw_args = sys.stdin.readline()
    args = raw_args.split()
    stack.process_command(args)
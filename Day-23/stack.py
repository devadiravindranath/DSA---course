class Stack:
    def __init__(self):
        self.stack = []

    # push
    def push(self, data):
        self.stack.append(data)

    # pop
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack.pop()

    # peek
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]

    # is_empty
    def is_empty(self):
        return len(self.stack) == 0

    # size
    def size(self):
        return len(self.stack)


# usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("top:", s.peek())
print("popped:", s.pop())
print("size:", s.size())
print("is empty:", s.is_empty())
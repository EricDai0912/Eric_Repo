class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop_with_item(self):
        item = self.stack[-1]
        self.stack.pop(-1)
        return item
    
    def pop(self):
        self.stack.pop(-1)

    def is_empty(self):
        count = 0
        for i in self.stack:
            count+=1
        if count == 0:
            return True
        else:
            return False
        
    def len(self):
        count = 0
        for i in self.stack:
            count+=1
        return count
    
    def peek(self):
        return self.stack[-1]

if __name__ == "__main__":
    # zk = Stack()
    # zk.push('a')
    # print(zk.stack)
    # zk.push('b')
    # print(zk.stack)
    # zk.pop()
    # print(zk.stack)

    zq = Stack()
    # print(zq.pop())
    # print(zq.stack)
    # print(zk.is_empty())
    # zk.pop()
    # print(zk.is_empty())
    # print(zq.len())
    # print(zq.peek())


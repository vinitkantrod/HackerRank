class Empty(Exception):
    pass

class Full(Exception):
    pass

class Stack:
    def __init__(self,length):
        self.data = []
        self.n = length
    
    def leng(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        return len(self.data) == self.n

    def push(self,e):
        if self.is_full():
            raise Full('Stack is Full')
        else:
            self.data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        else:
            return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        else:
            return self.data[-1]

if __name__ == "__main__":

    a = Stack(5)
    a.pop()
    a.push(4)
    print a.top()
    a.push(6)
    print a.top()
    a.pop()
    print a.top()
    print a.leng()    

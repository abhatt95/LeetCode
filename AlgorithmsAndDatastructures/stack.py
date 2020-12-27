class Stack:
    def __init__(self,n):
        self.stack = []
        self.size = n
        
    def peek(self):
        if not self.empty():
            return self.stack[-1]
        return -1

    def empty(self):
        if len(self.stack) > 0: return False
        return True
    
    def push(self,data):
        if len(self.stack) < self.size:
            self.stack.append(data)
        return -1
    
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return -1

    def print(self):
        print(self.stack)

    def sort(self):
        # Inspiration https://leetcode.com/discuss/interview-question/algorithms/125398/given-a-stack-sort-it-in-non-decreasing-order
        A = Stack(self.size)
        while not self.empty():
            current = self.pop()
            while not A.empty() and A.peek() < current: self.push(A.pop())
            A.push(current)
        while not A.empty(): self.push(A.pop())

s1 = Stack(5)
randomList = [2,5,3,1,7,6]
for num in randomList:
    s1.push(num)
s1.print()
print(s1.pop())
s1.push(randomList[-1])
s1.print()
s1.sort()
s1.print()
s1.pop()
s1.pop()
print(s1.peek())
s1.print()

class Heap:
    def __init__(self):
        self.heap = [-float('inf')]

    def insert(self,element):
        self.heap.append(element)
        k = len(self.heap)-1
        while k >=1 and self.heap[k] <= self.heap[k//2]: 
            self.heap[k],self.heap[k//2] = self.heap[k//2],self.heap[k]
            k = k//2
        #self.print()
    def getMin(self):
        if len(self.heap)>1: return self.heap[1]
        return -1

    def removeMin(self):
        minElement = -1
        if len(self.heap) > 1:
            self.heap[1],self.heap[-1] = self.heap[-1],self.heap[1]
            minElement = self.heap.pop()
            k = 1 
            while k < len(self.heap):
                min_index = k 
                l,r = 2*k,2*k + 1
                if l < len(self.heap) and self.heap[l] < self.heap[k]:
                    k = l
                if r < len(self.heap) and self.heap[r] < self.heap[k]:
                    k = r
                if min_index!=k:
                    self.heap[k],self.heap[min_index]=self.heap[min_index],self.heap[k]
                else: break
        return minElement 

    def print(self):
        print(self.heap)

    def hasElement(self):
        return len(self.heap) > 1
heap = Heap()

#inputs = [10,9,8,7,6,5,4,3,2,1]
inputs = [100,-99,0,-50,-999,0,10]
#inputs = []

for num in inputs:
    heap.insert(num)

#print(heap.getMin())
heap.print()
while heap.hasElement():
    print(heap.removeMin())
    heap.print()
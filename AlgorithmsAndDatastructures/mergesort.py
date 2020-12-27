class Solution:
    def combine(self,left,right):
        ans = []
        while left or right:
            if left and right:
                if left[0] < right[0]:
                    ans.append(left.pop(0))
                    continue
                ans.append(right.pop(0))
                continue
            if left: ans.append(left.pop(0))
            if right: ans.append(right.pop(0))
        return ans

    def mergeSort(self,array):
        # return empty or single element array as they are sorted
        if not array or len(array)==1:
            return array

        l = 0
        r = len(array)
        mid = (l+r)//2
        left = self.mergeSort(array[l:mid])
        right = self.mergeSort(array[mid:r])

        return self.combine(left,right)


s = Solution()
inputs = [[0,-10,-5,-20,-10,0,20,10,50,40],
          [],
          [-10]
            ]

for input in inputs:
    print(s.mergeSort(input))
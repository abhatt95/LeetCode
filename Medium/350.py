"""
Given two arrays, write a function to compute their intersection.


"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        index1 = 0
        index2 = 0
        
        output = []
        
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                output.append(nums1[index1])
                index1 += 1
                index2 += 1
                continue
            if nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1
                
        return output
                
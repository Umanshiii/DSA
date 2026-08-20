def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    num3=nums1+nums2
    n= len(num3)
    num3.sort()
    if n%2==0:
        median=(num3[n//2]+num3[(n//2)-1])/2
    else:
        median=num3[n//2]
    return median

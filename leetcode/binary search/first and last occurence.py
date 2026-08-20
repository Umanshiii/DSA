class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start, end = 0, n - 1
        first = last = -1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                first = mid
                end = mid - 1  
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                last = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return [first, last]
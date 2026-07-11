class Solution:
    def countFreq(self, arr, target):
        start, end = 0, len(arr) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] == target:
                res = 0
                left = mid
                while left >= 0 and arr[left] == target:
                    res += 1
                    left -= 1
                    
                right = mid + 1
                while right < len(arr) and arr[right] == target:
                    res += 1
                    right += 1
                    
                return res
                
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return 0
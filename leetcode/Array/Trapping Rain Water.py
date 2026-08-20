'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
def trap(self, height: List[int]) -> int:
    total = 0
    left = 0
    right = len(height) - 1
        
    leftMax = 0
    rightMax = 0
    while left < right:
            
        if height[left] < height[right]:
            
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                out = leftMax
                water = out - height[left]
                total += water                
                left += 1            
        else:        
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                out = rightMax
                water = out - height[right]
                total += water
                
            right -= 1
    return total

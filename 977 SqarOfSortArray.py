#977 Square of a Sorted Array

def sortedSquares(num):
    nums=[i**2 for i in range(0,len(num)+1)]
    left=0
    right=len(nums)
    while left>right:
        left[nums],right[nums]=right[nums],left[nums]
        left+=1
        right-=1
    
    return nums

num= [-1,-33,7,9,0,-8,5]
x = sortedSquares(num)
print(x)
'''
def sortedSquares(nums):
    # Square all the elements of the array
    squared = [x ** 2 for x in nums]
    
    # Sort the squared array
    squared.sort()
    
    return squared

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
'''
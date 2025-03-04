#167.Two Sum 11 - Input Array Is Sorted
#Input= number=[2,7,11,15],target = 9
#Output=[1,2],index number

def twoSum(number,target):
    n=len(number)
    left=0
    right=n-1
    while (left<right):
        sum=number[left]+number[right]
        if sum==target:
            return [left+1,right+1]
        elif sum<target:
            left+=1
        else:
            right-=1
    return number



#driver code
number = [2,7,11,15]
target=9
result=twoSum(number,target)
print(result)
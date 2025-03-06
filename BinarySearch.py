#function definition
def BinarySearch(arr,i,j,key):
    mid=i+(j-i)//2
    while(i<=j):
        if(key==arr[mid]):
            return True
        elif key>arr[mid]:
            i=mid+1
            mid=(i+j)//2
        else:
            j=mid-1
            mid=(i+j)//2
    return False
#Driver code
#n = int(input())
#arr=list(map(int,input().split()))
arr = [10,20,30,40,50,60,70,80]
key=30
result=BinarySearch(arr,0,len(arr)-1,key)
print(result)
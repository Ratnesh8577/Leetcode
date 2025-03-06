def reverseArray(n,arr,start,end):
    while (start<=end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

#Driver code
n = int(input("Enter the Array number: "))
arr=list(map(int,input().split()))
#arr=[10,20,30,40,50,60]
k=int(input("Enter the k "))
if (k>n):
    k=k%n
reverseArray(n,arr,0,n-1)
reverseArray(n,arr,0,k-1)
reverseArray(n,arr,k,n-1)
print(arr)

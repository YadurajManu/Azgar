a=[32,21,23,1,3,4,6,2]
n=int(input("enter"))
low,high=0,len(a)-1
while low<=high:
    mid=len(a)//2
    if a[mid]==n:
        print(mid)
    elif a[mid]<n:
        low=mid+1
    elif a[mid]>n:
        high=mid-1
    else:
        pass
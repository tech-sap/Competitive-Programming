#active cells and inactive cells.
arr = list(map(int, input().split()))
n = len(arr)
days = int(input())
for day in range(days):
    for i in range(n):
        if i==0:
            ps = arr[i]
            arr[i] = 0 ^ arr[i+1]
        elif i==n-1:
            arr[i] = ps^0
        else:
            ps1 = arr[i]
            arr[i] = ps^arr[i+1]
            ps = ps1
    
print(arr)

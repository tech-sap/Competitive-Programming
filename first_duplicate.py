#time-complexity :O(n)
#space-complexity : O(1)

def find_first_duplicate(arr):
    for i in range(len(arr)):
        if arr[arr[i]-1]<0:
            return abs(arr[i])
        else:
            arr[arr[i]-1] = -(abs(arr[arr[i]-1]))




arr = [1,2,1,3,3,1,5]
print(find_first_duplicate(arr))
print(arr)
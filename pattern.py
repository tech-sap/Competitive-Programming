num = int(input())

diff = num**2 + 1 

val = 0

for i in range(num):
    for spaces in range(i):
        print(' ',end=' ')
    for col1 in range(num-i):
        val += 1 
        print(val,end=' ')
        
    for col2 in range(diff, diff+num-i):
        print(col2,end=' ')
    diff -= (num - i - 1 )
    print()

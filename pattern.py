'''
pattern:
ip : 5
op :
1   2   3   4     5    26   27   28   29   30
    6   7    8     9    22   23   24   25
         10  11    12   19    20   21
              13    14   17   18
                     15   16
'''
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

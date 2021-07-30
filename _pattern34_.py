num = int(input())
q = 0
pos = 1
while num:
    if(num%2==0):
        q = 4*pos+q
        pos = pos*10
        num = num//2
        num = num-1
    else:
        q = 3*pos+q
        pos = pos*10
        num = num//2
print(q)

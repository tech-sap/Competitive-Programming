# ip: 27
#op :AA

#ip : 53
#op : BA

#ip : 26
#op : Z

num = int(input())
arr = []

while num:
      if num<=26:
            arr.insert(0,chr(64+num))
      else:
            arr.insert(0,chr(64+num%26))
      num = num//26

print(''.join(arr))

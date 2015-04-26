import math
sequence=input("输入待查找数列：")
a=input("需查找的数字为：")
low=0
high=len(sequence)-1
i=0
mide=0
while(low<high):
     i=i+1
     mid=(low+high)/2
     mid=int(math.ceil(mid))
     print('查找次数',i)
     print('the mid is',mid)
     print('the mid value is',sequence[mid])
     if a==sequence[mid]:
        print(sequence[mid])
        break
     elif  a>sequence[mid]:
           low=mid
     else:
         high=mid
if low>=high:
     print('NULL')
